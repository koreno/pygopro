#!/usr/bin/env python2

from contextlib import contextmanager
import urllib2
import time
import sys
import re

from crontab import CronTab

# author: Adrian Sitterle

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
url_photres_8M  = "/camera/PR?t={0}&p=%00"


# create a daily job for a specific time
def new_cron_specifictime(minute, hour, cmd):

    tab = CronTab(user=True)

    cron_job = tab.new(cmd, comment='via %s' % __file__)
    cron_job.minute.on(minute)
    cron_job.hour.on(hour)

    if not cron_job.is_valid():
        print tab.render()
        raise Exception("problem creating cron job")

    print tab.render()
    tab.write()


def new_cron_between(hour_start, hour_end, repeat_every, cmd):

    tab = CronTab(user=True)

    cron_job = tab.new(cmd, comment='via %s' % __file__)
    cron_job.minute.every(repeat_every)

    if hour_start < hour_end:
        cron_job.hour.during(hour_start, hour_end)

    if not cron_job.is_valid():
        print tab.render()
        raise Exception("problem creating cron job")

    print tab.render()
    tab.write()     


def sleep(s):
    for i in range(s, 0, -1):
        print i,
        sys.stdout.flush()
        time.sleep(1)
    print
    

class GoPro(object):

    def __init__(self, password):
        self.password = password

    def send_cmd(self, cmd):
        url = url_base + cmd.format(self.password)
        result = urllib2.urlopen(url).read()
        sleep(1)

    @contextmanager
    def awake(self):
        self.wake()
        try:
            yield self
        finally:
            self.sleep()

    def sleep(self):
        print "- sleep"
        self.send_cmd(url_gopro_off)

    def wake(self):
        print "- wake"
        self.send_cmd(url_gopro_on)
        sleep(5)        # wait till gopro wakes up

    def setup(self):
        print "- setup"
        self.send_cmd(url_vol_no)
        self.send_cmd(url_led_no)
        self.send_cmd(url_autooff_no)
        #self.send_cmd(url_photres_8M)

    def takepic(self):
        print "- takepic"
        self.send_cmd(url_mode_photo)
        sleep(5)        # wait for photo mode to turn on
        self.send_cmd(url_shutter_on)
        sleep(5)        # wait for photo to be taken
        self.download()

    def download(self):
        print "- download"
        url = url_base + url_media
        result = urllib2.urlopen(url).read()
        dirs = re.findall('href="(\d\d\dGOPRO)/"', result)
        if not dirs:
            raise Exception("No Media Folders")
        url += "/" + dirs[-1]
        result = urllib2.urlopen(url).read()
        pics = re.findall('href="(GOPR\d+\.JPG)"', result)
        if not pics:
            raise Exception("No Pictures")
        pic = max(pics)
        url += "/" + pic
        result = urllib2.urlopen(url)
        print "Downloading %s (%s bytes)..." % (pic, result.headers['content-length'])
        with open(pic, "wb") as f:
            while True:
                chunk = result.read(16*1024)
                if not chunk:
                    break
                f.write(chunk)
                print f.tell(), "\r",


def set_timelapse(args):
    print "seting up gopro for timelpase"
    # with GoPro(args.password).awake() as gopro:
    #     gopro.setup()
    from_, to = args.timespan

    import sys, os.path
    path = os.path.abspath(__file__)

    new_cron_between(from_, to, args.interval, "%s %s takepic" % (sys.executable, path))


def run_action(args):
    print "running action: ", args.action
    gopro = GoPro(args.password)
    with gopro.awake():
        func = getattr(gopro, args.action)()


if __name__=="__main__":

    import argparse

    parser = argparse.ArgumentParser(description='GoPro Commander')
    parser.add_argument('-p', '--password', type=str, required=True, help='GoPro WiFi Password')
    subparsers = parser.add_subparsers()

    parser_timelapse = subparsers.add_parser('timelapse')
    parser_timelapse.add_argument('-b', '--between', dest='timespan', metavar="HOUR", nargs=2, type=int, default=(0,0), help='Hours between which to do the TimeLapse')
    parser_timelapse.add_argument('interval', metavar='interval', type=int, help='The interval in minutes between photos')
    parser_timelapse.set_defaults(func=set_timelapse)

    for action in "setup sleep wake takepic".split():
        parser_action = subparsers.add_parser(action).set_defaults(func=run_action, action=action)

    args = parser.parse_args()
    args.func(args)

