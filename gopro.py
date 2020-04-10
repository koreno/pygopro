#!/usr/bin/env python3.7

from subprocess import check_call
from contextlib import contextmanager
from urllib.error import URLError
import urllib.request
import time
import sys
import re
import os

url_base = "http://10.5.5.9"
url_media = ":8080/videos/DCIM/"

url_gopro_on    = "/bacpac/PW?t={0}&p=%01"
url_gopro_off   = "/bacpac/PW?t={0}&p=%00"
url_shutter_on  = "/bacpac/SH?t={0}&p=%01"
url_shutter_off = "/bacpac/SH?t={0}&p=%00"
url_mode_video  = "/camera/CM?t={0}&p=%00"
url_mode_photo  = "/camera/CM?t={0}&p=%01"
url_fov_wide    = "/camera/FV?t={0}&p=%00"
url_fov_med     = "/camera/FV?t={0}&p=%01"
url_fov_narrow  = "/camera/FV?t={0}&p=%02"
url_vol_no      = "/camera/BS?t={0}&p=%00"
url_del_last    = "/camera/DL?t={0}&p=%00"
url_led_no      = "/camera/LB?t={0}&p=%00"
url_autooff_no  = "/camera/AO?t={0}&p=%00"
url_photres_7M  = "/camera/PR?t={0}&p=%04"
url_delete_last = "/camera/DL?t={0}"
url_delete_all  = "/camera/DA?t={0}"
url_status      = "/camera/se?t={0}"

SHOW_PROGRESS = sys.stdout.isatty()


# create a daily job for a specific time
def new_cron_specifictime(minute, hour, cmd):

    from crontab import CronTab

    tab = CronTab(user=True)

    cron_job = tab.new(cmd, comment=f'via {__file__}')
    cron_job.minute.on(minute)
    cron_job.hour.on(hour)

    print((tab.render()))
    if not cron_job.is_valid():
        raise Exception("problem creating cron job")

    tab.write()
    print("cron job installed")


def new_cron_between(hour_start, hour_end, repeat_every, cmd):

    from crontab import CronTab

    tab = CronTab(user=True)

    cron_job = tab.new(cmd, comment=f'via {__file__}')
    cron_job.minute.every(repeat_every)

    if hour_start < hour_end:
        cron_job.hour.during(hour_start, hour_end)

    print((tab.render()))
    if not cron_job.is_valid():
        raise Exception("problem creating cron job")

    tab.write()
    print("cron job installed")


if SHOW_PROGRESS:
    def go_sleep(s):
        for i in range(s, 0, -1):
            print(i, "\r", end=' ')
            sys.stdout.flush()
            time.sleep(1)
        print()
else:
    go_sleep = time.sleep


def wakeup(func):
    def f(self, *args, **kwargs):
        with self.awake():
            return func(self, *args, **kwargs)
    return f


class GoPro(object):

    def __init__(self, password):
        self.password = password
        self._awaked = 0

    def send_cmd(self, cmd, sleep=1):
        url = url_base + cmd.format(self.password)
        result = urllib.request.urlopen(url).read()
        go_sleep(sleep)
        return result

    @contextmanager
    def awake(self):
        if not self._awaked:
            self.wake()
        self._awaked += 1
        try:
            yield self
        finally:
            self._awaked -= 1
            if not self._awaked:
                self.off()

    def off(self):
        print("- off")
        self.send_cmd(url_gopro_off)

    def wake(self):
        print("- wake")
        self.send_cmd(url_gopro_on, sleep=5)
        # wait till gopro wakes up

    @wakeup
    def setup(self):
        print("- setup")
        self.send_cmd(url_vol_no)
        self.send_cmd(url_led_no)
        self.send_cmd(url_autooff_no)
        self.send_cmd(url_photres_7M)

    @wakeup
    def takepic(self):
        print("- takepic")
        self.send_cmd(url_mode_photo, sleep=5)
        # wait for photo mode to turn on
        self.send_cmd(url_shutter_on, sleep=5)
        # wait for photo to be taken

    @wakeup
    def download(self, last=True):
        print("- download")
        url = url_base + url_media
        result = urllib.request.urlopen(url).read()
        dirs = re.findall(r'href="(\d\d\dGOPRO)/"', result)
        if not dirs:
            raise Exception("No Media Folders")
        url += "/" + dirs[-1]
        result = urllib.request.urlopen(url).read()
        pics = re.findall(r'href="(GOPR\d+\.JPG)"', result)
        if not pics:
            raise Exception("No Pictures")

        def download_pic(url, pic):
            url += "/" + pic
            result = urllib.request.urlopen(url)
            print(f"Downloading {pic} ({result.headers['content-length']} bytes)...")
            with open(pic, "wb") as f:
                while True:
                    chunk = result.read(16*1024)
                    if not chunk:
                        break
                    f.write(chunk)
                    if SHOW_PROGRESS:
                        print(f.tell(), "\r", end=' ')
                if SHOW_PROGRESS:
                    sys.stdout.flush()
            return pic

        if last:
            return download_pic(url, max(pics))
        else:
            return [download_pic(url, pic) for pic in pics]

    @wakeup
    def delete(self, last=True):
        print("- delete")
        self.send_cmd(url_delete_last if last else url_delete_all, sleep=5)

    @wakeup
    def get_status(self):
        return self.send_cmd(url_status)

    def lapse(self):
        print("- lapse")
        with self.awake():
            self.takepic()
            pic = self.download(last=True)
            stat = self.get_status()
        stat_file = "gopro-status.dat"
        with open(stat_file, "wb") as f:
            f.write(stat)
        upload(stat_file)
        upload(pic)
        os.unlink(pic)


def execute(*params):
    try:
        check_call(params)
    except:
        print("error running: ", *params)
        raise


def resize(pic, ratio):
    print("- resizing image")
    params = ["-resize", f"{int(100 % ratio)}%", pic]
    if SHOW_PROGRESS:
        params.insert(0, "-monitor")
    execute("/usr/bin/mogrify", *params)


def make_timelapse(anim):
    print("- making animation")
    params = ["-morph", "3", "*.JPG", anim]
    if SHOW_PROGRESS:
        params.insert(0, "-monitor")
    execute("/usr/bin/convert", *params)


def upload(src):
    print((f"- upload ({src})"))
    params = ["upload", src, "."]
    if SHOW_PROGRESS:
        params.insert(0, "-p")
    execute("/usr/local/bin/dropbox_uploader.sh", *params)
    print("- done uploading")


def set_timelapse(args):
    if args.setup:
        print("seting up gopro for timelpase")
        with GoPro(args.password).awake() as gopro:
            gopro.setup()

    from_, to = args.timespan

    import sys
    import os.path
    path = os.path.abspath(__file__)

    new_cron_between(
        from_, to, args.interval,
        f"{sys.executable} {path} -p {args.password} lapse 2>&1 | logger -t gopro")


def run_action(args):
    print("running action: ", args.action)
    gopro = GoPro(args.password)
    func = getattr(gopro, args.action)
    func()


def restart():
    open("do_lapse", "w")
    os.system("sudo reboot")


if __name__ == "__main__":

    import argparse
    import socket

    parser = argparse.ArgumentParser(description='GoPro Commander')
    parser.add_argument('-p', '--password', type=str, help='GoPro WiFi Password')
    subparsers = parser.add_subparsers()

    parser_timelapse = subparsers.add_parser('timelapse')
    parser_timelapse.add_argument('-b', '--between', dest='timespan', metavar="HOUR", nargs=2, type=int, default=(0,0), help='Hours between which to do the TimeLapse')
    parser_timelapse.add_argument('-s', '--setup', action="store_true", help='Set up camera for timelapse (7MP Photo, no leds, no volume, no auto-off)')
    parser_timelapse.add_argument('interval', metavar='interval', type=int, help='The interval in minutes between photos')
    parser_timelapse.set_defaults(func=set_timelapse)

    for action in "setup sleep wake takepic lapse".split():
        parser_action = subparsers.add_parser(action).set_defaults(func=run_action, action=action)

    from commands import menu
    parser_action = subparsers.add_parser("menu").set_defaults(func=lambda args: menu(args.password))

    args = parser.parse_args()
    if not args.password:
        from getpass import getpass
        args.password = getpass("Enter WiFi password: ")

    try:
        args.func(args)
    except URLError as e:
        if isinstance(e.reason, socket.error) and e.reason.errno in (110, 113):
            restart()
        raise
