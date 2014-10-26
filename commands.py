def show_state(status):
    from .status import parse_status
    ret = parse_status(status)
    print(ret)
    raw_input("Enter to continue")
    return status


URL = "http://10.5.5.9/{0}/{1}?t={PASSWORD}&p=%{2}"

COMMANDS = {
    "Basics" : {
         "Turn GoPro OFF":         (("bacpac", "PW", "00"), None),
         "Turn GoPro ON":          (("bacpac", "PW", "01"), None),
         "Shutter":                (("bacpac", "SH", "01"), None),
         "Stop":                   (("bacpac", "SH", "00"), None),
         "Preview ON":             (("camera", "PV", "02"), None),
         "Preview OFF":            (("camera", "PV", "00"), None),
    },
    "Mode" : {
         "Video Mode":             (("camera", "CM", "00"), None),
         "Photo Mode":             (("camera", "CM", "01"), None),
         "Burst Mode":             (("camera", "CM", "02"), None),
         "Timelapse Mode":         (("camera", "CM", "03"), None),
         "Timer Mode (hero2)":     (("camera", "CM", "04"), None),
         "Play HDMI":              (("camera", "CM", "05"), None),
    },
    "Orientation" : {
         "Orientation UP":         (("camera", "UP", "00"), None),
         "Orientation DOWN":       (("camera", "UP", "01"), None),
    },
    "Video resolutions HERO2 and HERO3 silver" : {
         "WVGA 60":                (("camera", "VR", "00"), None),
         "WVGA 120":               (("camera", "VR", "01"), None),
         "720 30":                 (("camera", "VR", "02"), None),
         "720 60":                 (("camera", "VR", "03"), None),
         "960 30":                 (("camera", "VR", "04"), None),
         "960 48":                 (("camera", "VR", "05"), None),
         "1080 30":                (("camera", "VR", "06"), None),
    },
    "Video resolutions Black edition" : {
         "4kCin12":                (("camera", "VV", "08"), None),
         "2.7kCin24":              (("camera", "VV", "07"), None),
         "4k 15":                  (("camera", "VV", "06"), None),
         "2.7k 30":                (("camera", "VV", "05"), None),
         "1440p 40":               (("camera", "VV", "04"), None),
         "1080 60":                (("camera", "VV", "03"), None),
         "1080 30":                (("camera", "VR", "05"), None),
         "960 48":                 (("camera", "VR", "06"), None),
         "960 100":                (("camera", "VV", "02"), None),
         "720 120":                (("camera", "VV", "01"), None),
         "WVGA 240":               (("camera", "VV", "00"), None),
    },
    "Video resolutions HERO3+Black" : {
        "4K":                      (("camera", "VV", "06"), None),
        "4K 17:9":                 (("camera", "VV", "08"), None),
        "4K 15FPS":                (("camera", "FS", "01"), None),
        "4K 12FPS":                (("camera", "FS", "00"), None),
        "2.7k":                    (("camera", "VV", "05"), None),
        "2.7k 24FPS":              (("camera", "FS", "02"), None),
        "2.7k 30FPS":              (("camera", "FS", "04"), None),
        "2K":                      (("camera", "VV", "07"), None),
        "1440p":                   (("camera", "VV", "04"), None),
        "1440 48FPS":              (("camera", "FS", "05"), None),
        "1080 SuperView":          (("camera", "VV", "09"), None),
        "1080":                    (("camera", "VV", "03"), None),
        "960p":                    (("camera", "VV", "02"), None),
        "720 SuperView":           (("camera", "VV", "0a"), None),
        "720p":                    (("camera", "VV", "01"), None),
    },
    "Frame rate" : {
         "FPS12":                  (("camera", "FS", "00"), None),
         "FPS15":                  (("camera", "FS", "01"), None),
         "FPS12p5":                (("camera", "FS", "0b"), None),
         "FPS24":                  (("camera", "FS", "02"), None),
         "FPS25":                  (("camera", "FS", "03"), None),
         "FPS30":                  (("camera", "FS", "04"), None),
         "FPS4":                   (("camera", "FS", "05"), None),
         "FPS50":                  (("camera", "FS", "06"), None),
         "FPS60":                  (("camera", "FS", "07"), None),
         "FPS100":                 (("camera", "FS", "08"), None),
         "FPS120":                 (("camera", "FS", "09"), None),
         "FPS240":                 (("camera", "FS", "0a"), None),
    },
    "Fov" : {
         "wide":                   (("camera", "FV", "00"), None),
         "medium":                 (("camera", "FV", "01"), None),
         "narrow":                 (("camera", "FV", "02"), None),
    },
    "Photo resolution HERO2 and HERO3 silver" : {
         "11mpW":                  (("camera", "PR", "00"), None),
         "8mpM":                   (("camera", "PR", "01"), None),
         "5mpW":                   (("camera", "PR", "02"), None),
         "5mpM":                   (("camera", "PR", "03"), None),
    },
    "Timelapse Interval" : {
         "0,5 sec":                (("camera", "TI", "00"), None),
         "1sec":                   (("camera", "TI", "01"), None),
         "5sec":                   (("camera", "TI", "05"), None),
         "10sec":                  (("camera", "TI", "0a"), None),
         "30sec":                  (("camera", "TI", "1e"), None),
         "60sec":                  (("camera", "TI", "3c"), None),
    },
    "Volume" : {
         "no sound":               (("camera", "BS", "00"), None),
         "70%":                    (("camera", "BS", "01"), None),
         "100%":                   (("camera", "BS", "02"), None),
    },
    "White Balance HERO3 ONLY IF Protune ON" : {
         "auto":                   (("camera", "WB", "00"), None),
         "3000k":                  (("camera", "WB", "01"), None),
         "5500k":                  (("camera", "WB", "02"), None),
         "6500k":                  (("camera", "WB", "03"), None),
         "CAMRAW":                 (("camera", "WB", "04"), None),
    },
    "Continuous Shot (HERO3)" : {
         "Single":                 (("camera", "CS", "00"), None),
         "3SPS":                   (("camera", "CS", "03"), None),
         "5SPS":                   (("camera", "CS", "05"), None),
         "10SPS":                  (("camera", "CS", "0a"), None),
    },
    "Burst Rate HERO3" : {
         "3/1s":                   (("camera", "BU", "00"), None),
         "10/1s":                  (("camera", "BU", "02"), None),
         "10/2s":                  (("camera", "BU", "03"), None),
         "30/1s":                  (("camera", "BU", "04"), None),
         "30/2s":                  (("camera", "BU", "05"), None),
         "30/3s":                  (("camera", "BU", "06"), None),
    },
    "Loop Video HERO3" : {
         "OFF":                    (("camera", "LO", "00"), None),
         "5min":                   (("camera", "LO", "01"), None),
         "20Min":                  (("camera", "LO", "02"), None),
         "60Min":                  (("camera", "LO", "03"), None),
         "Max":                    (("camera", "LO", "05"), None),
    },
    "Protune ON/OFF" : {
         "ON":                     (("camera", "PT", "01"), None),
         "OFF":                    (("camera", "PT", "00"), None),
    },
    "Delete" : {
         "last":                   (( "camera", "DL"), None),
         "all":                    (( "camera", "DA"), None),
    },
    "Photo resolution Black ed" : {
         "12mpW":                  (("camera", "PR", "05"), None),
         "7mpW":                   (("camera", "PR", "04"), None),
         "7mpM":                   (("camera", "PR", "06"), None),
         "5mpM":                   (("camera", "PR", "03"), None),
    },
    "Leds" : {
         "no leds":                (("bacpac", "LB", "00"), None),
         "2 leds":                 (("camera", "LB", "01"), None),
         "4 leds":                 (("camera", "LB", "02"), None),
    },
    "Spot Meter" : {
         "OFF":                    (("camera", "EX", "00"), None),
         "ON":                     (("camera", "EX", "01"), None),
    },
    "One Button Mode" : {
         "OFF":                    (("camera", "OB", "00"), None),
         "ON":                     (("camera", "OB", "01"), None),
    },
    "Protune Resolutions HERO2 and HERO3 silver" : {
         "1080 30 Protune":        (("camera", "VR", "07"), None),
         "1080 24 Protune":        (("camera", "VR", "08"), None),
         "1080 25 Protune":        (("camera", "VR", "11"), None),
         "960 60 Protune":         (("camera", "VR", "09"), None),
    },
    "Protune Resolutions HERO3 black ONLY IF PROTUNE IS ON" : {
         "720 120T":               (("camera", "VV", "00"), None),
         "960 100T":               (("camera", "VV", "02"), None),
         "1080 60T":               (("camera", "VV", "03"), None),
         "1440 48T":               (("camera", "VV", "04"), None),
         "2.7k 30T":               (("camera", "VV", "05"), None),
         "4k 15T":                 (("camera", "VV", "06"), None),
         "2.7KCin24T":             (("camera", "VV", "07"), None),
         "4kCin12T":               (("camera", "VV", "08"), None),
    },
    "Auto Power Off" : {
         "NEVER":                  (("camera", "AO", "00"), None),
         "60s":                    (("camera", "AO", "01"), None),
         "120s":                   (("camera", "AO", "02"), None),
         "300s":                   (("camera", "AO", "03"), None),
    },
    "Default Mode" : {
         "Video":                  (("camera", "DM", "00"), None),
         "Photo":                  (("camera", "DM", "01"), None),
         "Burst":                  (("camera", "DM", "02"), None),
         "Timelapse":              (("camera", "DM", "03"), None),
    },
    "OnScreen Display" : {
         "OFF":                    (("camera", "OS", "00"), None),
         "ON":                     (("camera", "OS", "01"), None),
    },
    "Locate" : {
         "Start":                  (("camera", "LL", "01"), None),
         "Stop":                   (("camera", "LL", "00"), None),
    },
    "Video Mode" : {
         "NTSC":                   (("camera", "VM", "00"), None),
         "PAL":                    (("camera", "VM", "01"), None),
    },
    "State" : {
        "state":                   (("camera", "se"), show_state),
        "name":                    (("camera", "cv"), str),
        "password":                (("camera", "sd"), str),
    }
}


def menu(password):

    from functools import partial
    from menu import AppMenu
    import requests

    def make_action(params):
        def action():
            url = URL.format(*params, PASSWORD=password)
            print url,
            ret = requests.get(url)
            print ret
        return action

    def convert(d, typ):
        if isinstance(d, dict):
            return dict(zip(d, (convert(v, typ) for v in d.itervalues())))
        return typ(d)

    def menu(title, d):
        if isinstance(d, dict):
            AppMenu.show_menu(title, [
                (name, partial(menu, "%s >> %s" % (title, name), value))
                for name, value in sorted(d.items())
            ])
        elif callable(d):
            d()
        else:
            print(d)

    action_tree = convert(COMMANDS, make_action)
    menu("GoPro", action_tree)
