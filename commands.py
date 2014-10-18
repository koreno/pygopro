

COMMANDS = {
    "Basics" : {
         "Turn GoPro OFF":         ("bacpac", "PW", "00"),
         "Turn GoPro ON":          ("bacpac", "PW", "01"),
         "Shutter":                ("bacpac", "SH", "01"),
         "Stop":                   ("bacpac", "SH", "00"),
         "Preview ON":             ("camera", "PV", "02"),
         "Preview OFF":            ("camera", "PV", "00"),
    },
    "Mode" : {
         "Video Mode":             ("camera", "CM", "00"),
         "Photo Mode":             ("camera", "CM", "01"),
         "Burst Mode":             ("camera", "CM", "02"),
         "Timelapse Mode":         ("camera", "CM", "03"),
         "Timer Mode (hero2)":     ("camera", "CM", "04"),
         "Play HDMI":              ("camera", "CM", "05"),
    },
    "Orientation" : {
         "Orientation UP":         ("camera", "UP", "00"),
         "Orientation DOWN":       ("camera", "UP", "01"),
    },
    "Video resolutions HERO2 and HERO3 silver" : {
         "WVGA 60":                ("camera", "VR", "00"),
         "WVGA 120":               ("camera", "VR", "01"),
         "720 30":                 ("camera", "VR", "02"),
         "720 60":                 ("camera", "VR", "03"),
         "960 30":                 ("camera", "VR", "04"),
         "960 48":                 ("camera", "VR", "05"),
         "1080 30":                ("camera", "VR", "06"),
    },
    "Video resolutions Black edition" : {
         "4kCin12":                ("camera", "VV", "08"),
         "2.7kCin24":              ("camera", "VV", "07"),
         "4k 15":                  ("camera", "VV", "06"),
         "2.7k 30":                ("camera", "VV", "05"),
         "1440p 40":               ("camera", "VV", "04"),
         "1080 60":                ("camera", "VV", "03"),
         "1080 30":                ("camera", "VR", "05"),
         "960 48":                 ("camera", "VR", "06"),
         "960 100":                ("camera", "VV", "02"),
         "720 120":                ("camera", "VV", "01"),
         "WVGA 240":               ("camera", "VV", "00"),
    },
    "Video resolutions HERO3+Black" : {
        "4K":                      ("camera", "VV", "06"),
        "4K 17:9":                 ("camera", "VV", "08"),
        "4K 15FPS":                ("camera", "FS", "01"),
        "4K 12FPS":                ("camera", "FS", "00"),
        "2.7k":                    ("camera", "VV", "05"),
        "2.7k 24FPS":              ("camera", "FS", "02"),
        "2.7k 30FPS":              ("camera", "FS", "04"),
        "2K":                      ("camera", "VV", "07"),
        "1440p":                   ("camera", "VV", "04"),
        "1440 48FPS":              ("camera", "FS", "05"),
        "1080 SuperView":          ("camera", "VV", "09"),
        "1080":                    ("camera", "VV", "03"),
        "960p":                    ("camera", "VV", "02"),
        "720 SuperView":           ("camera", "VV", "0a"),
        "720p":                    ("camera", "VV", "01"),
    },
    "Frame rate" : {
         "FPS12":                  ("camera", "FS", "00"),
         "FPS15":                  ("camera", "FS", "01"),
         "FPS12p5":                ("camera", "FS", "0b"),
         "FPS24":                  ("camera", "FS", "02"),
         "FPS25":                  ("camera", "FS", "03"),
         "FPS30":                  ("camera", "FS", "04"),
         "FPS4":                   ("camera", "FS", "05"),
         "FPS50":                  ("camera", "FS", "06"),
         "FPS60":                  ("camera", "FS", "07"),
         "FPS100":                 ("camera", "FS", "08"),
         "FPS120":                 ("camera", "FS", "09"),
         "FPS240":                 ("camera", "FS", "0a"),
    },
    "Fov" : {
         "wide":                   ("camera", "FV", "00"),
         "medium":                 ("camera", "FV", "01"),
         "narrow":                 ("camera", "FV", "02"),
    },
    "Photo resolution HERO2 and HERO3 silver" : {
         "11mpW":                  ("camera", "PR", "00"),
         "8mpM":                   ("camera", "PR", "01"),
         "5mpW":                   ("camera", "PR", "02"),
         "5mpM":                   ("camera", "PR", "03"),
    },
    "Timelapse Interval" : {
         "0,5 sec":                ("camera", "TI", "00"),
         "1sec":                   ("camera", "TI", "01"),
         "5sec":                   ("camera", "TI", "05"),
         "10sec":                  ("camera", "TI", "0a"),
         "30sec":                  ("camera", "TI", "1e"),
         "60sec":                  ("camera", "TI", "3c"),
    },
    "Volume" : {
         "no sound":               ("camera", "BS", "00"),
         "70%":                    ("camera", "BS", "01"),
         "100%":                   ("camera", "BS", "02"),
    },
    "White Balance HERO3 ONLY IF Protune ON" : {
         "auto":                   ("camera", "WB", "00"),
         "3000k":                  ("camera", "WB", "01"),
         "5500k":                  ("camera", "WB", "02"),
         "6500k":                  ("camera", "WB", "03"),
         "CAMRAW":                 ("camera", "WB", "04"),
    },
    "Continuous Shot (HERO3)" : {
         "Single":                 ("camera", "CS", "00"),
         "3SPS":                   ("camera", "CS", "03"),
         "5SPS":                   ("camera", "CS", "05"),
         "10SPS":                  ("camera", "CS", "0a"),
    },
    "Burst Rate HERO3" : {
         "3/1s":                   ("camera", "BU", "00"),
         "10/1s":                  ("camera", "BU", "02"),
         "10/2s":                  ("camera", "BU", "03"),
         "30/1s":                  ("camera", "BU", "04"),
         "30/2s":                  ("camera", "BU", "05"),
         "30/3s":                  ("camera", "BU", "06"),
    },
    "Loop Video HERO3" : {
         "OFF":                    ("camera", "LO", "00"),
         "5min":                   ("camera", "LO", "01"),
         "20Min":                  ("camera", "LO", "02"),
         "60Min":                  ("camera", "LO", "03"),
         "Max":                    ("camera", "LO", "05"),
    },
    "Protune ON/OFF" : {
         "ON":                     ("camera", "PT", "01"),
         "OFF":                    ("camera", "PT", "00"),
    },
    "Delete" : {
         "last":                   ( "camera", "DL", "?"),
         "all":                    ( "camera", "DA", "?"),
    },
    "Photo resolution Black ed" : {
         "12mpW":                  ("camera", "PR", "05"),
         "7mpW":                   ("camera", "PR", "04"),
         "7mpM":                   ("camera", "PR", "06"),
         "5mpM":                   ("camera", "PR", "03"),
    },
    "Leds" : {
         "no leds":                ("bacpac", "LB", "00"),
         "2 leds":                 ("camera", "LB", "01"),
         "4 leds":                 ("camera", "LB", "02"),
    },
    "Spot Meter" : {
         "OFF":                    ("camera", "EX", "00"),
         "ON":                     ("camera", "EX", "01"),
    },
    "One Button Mode" : {
         "OFF":                    ("camera", "OB", "00"),
         "ON":                     ("camera", "OB", "01"),
    },
    "Protune Resolutions HERO2 and HERO3 silver" : {
         "1080 30 Protune":        ("camera", "VR", "07"),
         "1080 24 Protune":        ("camera", "VR", "08"),
         "1080 25 Protune":        ("camera", "VR", "11"),
         "960 60 Protune":         ("camera", "VR", "09"),
    },
    "Protune Resolutions HERO3 black ONLY IF PROTUNE IS ON" : {
         "720 120T":               ("camera", "VV", "00"),
         "960 100T":               ("camera", "VV", "02"),
         "1080 60T":               ("camera", "VV", "03"),
         "1440 48T":               ("camera", "VV", "04"),
         "2.7k 30T":               ("camera", "VV", "05"),
         "4k 15T":                 ("camera", "VV", "06"),
         "2.7KCin24T":             ("camera", "VV", "07"),
         "4kCin12T":               ("camera", "VV", "08"),
    },
    "Auto Power Off" : {
         "NEVER":                  ("camera", "AO", "00"),
         "60s":                    ("camera", "AO", "01"),
         "120s":                   ("camera", "AO", "02"),
         "300s":                   ("camera", "AO", "03"),
    },
    "Default Mode" : {
         "Video":                  ("camera", "DM", "00"),
         "Photo":                  ("camera", "DM", "01"),
         "Burst":                  ("camera", "DM", "02"),
         "Timelapse":              ("camera", "DM", "03"),
    },
    "OnScreen Display" : {
         "OFF":                    ("camera", "OS", "00"),
         "ON":                     ("camera", "OS", "01"),
    },
    "Locate" : {
         "Start":                  ("camera", "LL", "01"),
         "Stop":                   ("camera", "LL", "00"),
    },
    "Video Mode" : {
         "NTSC":                   ("camera", "VM", "00"),
         "PAL":                    ("camera", "VM", "01"),
    },
}

URL = "http://10.5.5.9/{0}/{1}?t={PASSWORD}&p=%{2}"


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
