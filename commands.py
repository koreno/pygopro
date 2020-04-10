from collections import namedtuple


class Action(namedtuple("Action", "params callback", defaults=[None])):
    pass


def show_state(status):
    from status import parse_status
    ret = parse_status(status)
    print(ret)
    input("Enter to continue")
    return status


URL = "http://10.5.5.9/{0}/{1}?t={PASSWORD}"

COMMANDS = {
    "Basics": {
        "Turn GoPro OFF":         Action(("bacpac", "PW", "00")),
        "Turn GoPro ON":          Action(("bacpac", "PW", "01")),
        "Shutter":                Action(("bacpac", "SH", "01")),
        "Stop":                   Action(("bacpac", "SH", "00")),
        "Preview ON":             Action(("camera", "PV", "02")),
        "Preview OFF":            Action(("camera", "PV", "00")),
    },
    "Mode": {
        "Video Mode":             Action(("camera", "CM", "00")),
        "Photo Mode":             Action(("camera", "CM", "01")),
        "Burst Mode":             Action(("camera", "CM", "02")),
        "Timelapse Mode":         Action(("camera", "CM", "03")),
        "Timer Mode (hero2)":     Action(("camera", "CM", "04")),
        "Play HDMI":              Action(("camera", "CM", "05")),
    },
    "Orientation": {
        "Orientation UP":         Action(("camera", "UP", "00")),
        "Orientation DOWN":       Action(("camera", "UP", "01")),
    },
    "Video resolutions HERO2 and HERO3 silver": {
        "WVGA 60":                Action(("camera", "VR", "00")),
        "WVGA 120":               Action(("camera", "VR", "01")),
        "720 30":                 Action(("camera", "VR", "02")),
        "720 60":                 Action(("camera", "VR", "03")),
        "960 30":                 Action(("camera", "VR", "04")),
        "960 48":                 Action(("camera", "VR", "05")),
        "1080 30":                Action(("camera", "VR", "06")),
    },
    "Video resolutions Black edition": {
        "4kCin12":                Action(("camera", "VV", "08")),
        "2.7kCin24":              Action(("camera", "VV", "07")),
        "4k 15":                  Action(("camera", "VV", "06")),
        "2.7k 30":                Action(("camera", "VV", "05")),
        "1440p 40":               Action(("camera", "VV", "04")),
        "1080 60":                Action(("camera", "VV", "03")),
        "1080 30":                Action(("camera", "VR", "05")),
        "960 48":                 Action(("camera", "VR", "06")),
        "960 100":                Action(("camera", "VV", "02")),
        "720 120":                Action(("camera", "VV", "01")),
        "WVGA 240":               Action(("camera", "VV", "00")),
    },
    "Video resolutions HERO3+Black": {
        "4K":                      Action(("camera", "VV", "06")),
        "4K 17:9":                 Action(("camera", "VV", "08")),
        "4K 15FPS":                Action(("camera", "FS", "01")),
        "4K 12FPS":                Action(("camera", "FS", "00")),
        "2.7k":                    Action(("camera", "VV", "05")),
        "2.7k 24FPS":              Action(("camera", "FS", "02")),
        "2.7k 30FPS":              Action(("camera", "FS", "04")),
        "2K":                      Action(("camera", "VV", "07")),
        "1440p":                   Action(("camera", "VV", "04")),
        "1440 48FPS":              Action(("camera", "FS", "05")),
        "1080 SuperView":          Action(("camera", "VV", "09")),
        "1080":                    Action(("camera", "VV", "03")),
        "960p":                    Action(("camera", "VV", "02")),
        "720 SuperView":           Action(("camera", "VV", "0a")),
        "720p":                    Action(("camera", "VV", "01")),
    },
    "Frame rate": {
        "FPS12":                  Action(("camera", "FS", "00")),
        "FPS15":                  Action(("camera", "FS", "01")),
        "FPS12p5":                Action(("camera", "FS", "0b")),
        "FPS24":                  Action(("camera", "FS", "02")),
        "FPS25":                  Action(("camera", "FS", "03")),
        "FPS30":                  Action(("camera", "FS", "04")),
        "FPS4":                   Action(("camera", "FS", "05")),
        "FPS50":                  Action(("camera", "FS", "06")),
        "FPS60":                  Action(("camera", "FS", "07")),
        "FPS100":                 Action(("camera", "FS", "08")),
        "FPS120":                 Action(("camera", "FS", "09")),
        "FPS240":                 Action(("camera", "FS", "0a")),
    },
    "Fov": {
        "wide":                   Action(("camera", "FV", "00")),
        "medium":                 Action(("camera", "FV", "01")),
        "narrow":                 Action(("camera", "FV", "02")),
    },
    "Photo resolution HERO2 and HERO3 silver": {
        "11mpW":                  Action(("camera", "PR", "00")),
        "8mpM":                   Action(("camera", "PR", "01")),
        "5mpW":                   Action(("camera", "PR", "02")),
        "5mpM":                   Action(("camera", "PR", "03")),
    },
    "Timelapse Interval": {
        "0,5 sec":                Action(("camera", "TI", "00")),
        "1sec":                   Action(("camera", "TI", "01")),
        "5sec":                   Action(("camera", "TI", "05")),
        "10sec":                  Action(("camera", "TI", "0a")),
        "30sec":                  Action(("camera", "TI", "1e")),
        "60sec":                  Action(("camera", "TI", "3c")),
    },
    "Volume": {
        "no sound":               Action(("camera", "BS", "00")),
        "70%":                    Action(("camera", "BS", "01")),
        "100%":                   Action(("camera", "BS", "02")),
    },
    "White Balance HERO3 ONLY IF Protune ON": {
        "auto":                   Action(("camera", "WB", "00")),
        "3000k":                  Action(("camera", "WB", "01")),
        "5500k":                  Action(("camera", "WB", "02")),
        "6500k":                  Action(("camera", "WB", "03")),
        "CAMRAW":                 Action(("camera", "WB", "04")),
    },
    "Continuous Shot (HERO3)": {
        "Single":                 Action(("camera", "CS", "00")),
        "3SPS":                   Action(("camera", "CS", "03")),
        "5SPS":                   Action(("camera", "CS", "05")),
        "10SPS":                  Action(("camera", "CS", "0a")),
    },
    "Burst Rate HERO3": {
        "3/1s":                   Action(("camera", "BU", "00")),
        "10/1s":                  Action(("camera", "BU", "02")),
        "10/2s":                  Action(("camera", "BU", "03")),
        "30/1s":                  Action(("camera", "BU", "04")),
        "30/2s":                  Action(("camera", "BU", "05")),
        "30/3s":                  Action(("camera", "BU", "06")),
    },
    "Loop Video HERO3": {
        "OFF":                    Action(("camera", "LO", "00")),
        "5min":                   Action(("camera", "LO", "01")),
        "20Min":                  Action(("camera", "LO", "02")),
        "60Min":                  Action(("camera", "LO", "03")),
        "Max":                    Action(("camera", "LO", "05")),
    },
    "Protune ON/OFF": {
        "ON":                     Action(("camera", "PT", "01")),
        "OFF":                    Action(("camera", "PT", "00")),
    },
    "Delete": {
        "last":                   Action(( "camera", "DL")),
        "all":                    Action(( "camera", "DA")),
    },
    "Photo resolution Black ed": {
        "12mpW":                  Action(("camera", "PR", "05")),
        "7mpW":                   Action(("camera", "PR", "04")),
        "7mpM":                   Action(("camera", "PR", "06")),
        "5mpM":                   Action(("camera", "PR", "03")),
    },
    "Leds": {
        "no leds":                Action(("bacpac", "LB", "00")),
        "2 leds":                 Action(("camera", "LB", "01")),
        "4 leds":                 Action(("camera", "LB", "02")),
    },
    "Spot Meter": {
        "OFF":                    Action(("camera", "EX", "00")),
        "ON":                     Action(("camera", "EX", "01")),
    },
    "One Button Mode": {
        "OFF":                    Action(("camera", "OB", "00")),
        "ON":                     Action(("camera", "OB", "01")),
    },
    "Protune Resolutions HERO2 and HERO3 silver": {
        "1080 30 Protune":        Action(("camera", "VR", "07")),
        "1080 24 Protune":        Action(("camera", "VR", "08")),
        "1080 25 Protune":        Action(("camera", "VR", "11")),
        "960 60 Protune":         Action(("camera", "VR", "09")),
    },
    "Protune Resolutions HERO3 black ONLY IF PROTUNE IS ON": {
        "720 120T":               Action(("camera", "VV", "00")),
        "960 100T":               Action(("camera", "VV", "02")),
        "1080 60T":               Action(("camera", "VV", "03")),
        "1440 48T":               Action(("camera", "VV", "04")),
        "2.7k 30T":               Action(("camera", "VV", "05")),
        "4k 15T":                 Action(("camera", "VV", "06")),
        "2.7KCin24T":             Action(("camera", "VV", "07")),
        "4kCin12T":               Action(("camera", "VV", "08")),
    },
    "Auto Power Off": {
        "NEVER":                  Action(("camera", "AO", "00")),
        "60s":                    Action(("camera", "AO", "01")),
        "120s":                   Action(("camera", "AO", "02")),
        "300s":                   Action(("camera", "AO", "03")),
    },
    "Default Mode": {
        "Video":                  Action(("camera", "DM", "00")),
        "Photo":                  Action(("camera", "DM", "01")),
        "Burst":                  Action(("camera", "DM", "02")),
        "Timelapse":              Action(("camera", "DM", "03")),
    },
    "OnScreen Display": {
        "OFF":                    Action(("camera", "OS", "00")),
        "ON":                     Action(("camera", "OS", "01")),
    },
    "Locate": {
        "Start":                  Action(("camera", "LL", "01")),
        "Stop":                   Action(("camera", "LL", "00")),
    },
    "Video Mode": {
        "NTSC":                   Action(("camera", "VM", "00")),
        "PAL":                    Action(("camera", "VM", "01")),
    },
    "State": {
        "state":                   Action(("camera", "se"), show_state),
        "name":                    Action(("camera", "cv"), str),
        "password":                Action(("camera", "sd"), str),
    }
}


def menu(password):

    from termenu.app import AppMenu
    import requests

    def make_action(act):
        params = act.params

        def action():
            assert len(params) <= 3
            url = URL.format(*params[:2], PASSWORD=password)
            if len(params) > 2:
                url += "&p=%" + params[2]
            print(url, "->", end=' ')
            ret = requests.get(url)
            print(ret, "->", end=' ')
            if act.callback:
                print("...")
                return act.callback(ret.content)
            else:
                print(repr(ret.content))
        return action

    def convert(d, typ, parents=[]):
        if isinstance(d, dict):
            for (k, v) in sorted(d.items()):
                for item in convert(v, make_action, parents=parents + [k]):
                    yield item
        else:
            yield " - ".join(parents), typ(d)

    actions = sorted(convert(COMMANDS, make_action))
    AppMenu.show("GoPro", actions)
