from construct import Struct, Byte, Padding, Flag, Enum, EmbeddedBitStruct, UBInt16


STATUS = Struct("GoProStatus",

    # 1 ?
    Padding(1),

    # 2 Current mode. 0-4 matches set CM. 7 - in menu.
    Enum(Byte("mode"), video=0, photo=1, burst=2, timelapse=3, timer=4, play=5, menu=7 ),

    # 3 ?
    Padding(1),

    # 4 Start up mode : 0 = video - 1 = photo - 2 = burst - 3 = timelapse
    Enum(Byte("startup_mode"), video=0, photo=1, burst=2, timelapse=3),

    # 5 Spot meter : 0 = Off - 1 = On
    Flag("spot"),

    # 6 Current timelapse interval
    Byte("timelapse_interval"),

    # 7 Automatic power off : 0 = never - 1 = 60sec - 2 = 120sec - 3 = 300sec
    Enum(Byte("auto_off"), never=0, **{"60": 1, "120": 2, "300": 3}),

    # 8 Current view angle
    Byte("view_angle"),

    # 9 Current photo mode
    Byte("photo_mode"),

    # 10    Current video mode
    Byte("video_mode"),

    # 11    ?
    # 12    ?
    # 13    ?
    Padding(3),

    # 14    Recording minutes
    Byte("recording_minutes"),

    # 15    Recording seconds
    Byte("recording_seconds"),

    # 16    ?
    Padding(1),

    # 17    Current beep volume
    Byte("beep_volume"),

    # 18    2 = 4 LEDS - 1 = 2 LEDS - 0 = LEDS off
    Enum(Byte("leds"), **{"4": 2, "2": 1, "0": 0}),

    # 19
    EmbeddedBitStruct(
        #   bit 1 : 1 = preview on - 0 = preview off
        Flag("preview"),
        #   bit 2 : ?
        Padding(1),
        #   bit 3 : 0 = up - 1 = down
        Flag("inverted"),
        #   bit 4 : 1 = one button on - 0 = one button off
        Flag("one_button"),
        #   bit 5 : 1 = OSD on - 0 = OSD off
        Flag("OSD"),
        #   bit 6 : 0 = NTSC - 1 = PAL
        Enum(Flag("output_feed"), NTSC=0, PAL=1),
        #   bit 7 : 1 = Locate(beeping)
        Flag("locating"),
        #   bit 8 : ?
        Padding(1),
    ),

    # 20    Battery %
    Byte("battery"),

    # 21    ?
    Padding(1),

    Struct("storage",

        # 22    Photos available (hi byte) or 255 = no SD Card
        # 23    Photos available (lo byte)
        UBInt16("photos_remain"),

        # 24    Photo count (hi byte)
        # 25    Photo count (lo byte)
        UBInt16("photos"),

        # 26    Video Time Remaining in minutes (hi byte)
        # 27    Video Time Left (lo byte)
        UBInt16("time_remain"),

        # 28    Video count (hi byte)
        # 29    Video count (lo byte)
        UBInt16("videos"),

        # 30    Recording
        Flag("recording"),
    ),

    # 31    ?
    Padding(1),
)


parse_status = STATUS.parse