# wave - play around with creating a WAVE file

Buffer up samples from `arecord(3)` and create a `.wav` file from them.

This uses the default sound source, which in my immediate case is
a crappy laptop mic.

```
$ arecord -l
**** List of CAPTURE Hardware Devices ****
card 0: PCH [HDA Intel PCH], device 0: CX20590 Analog [CX20590 Analog]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

Here's also where I discover that the USB mini cable for an old USB
condensor mic has gone missing. mini? Jeez.

```

$ arecord -L
null
    Discard all samples (playback) or generate zero samples (capture)
pipewire
    PipeWire Sound Server
default
    Default ALSA Output (currently PipeWire Media Server)
hw:CARD=PCH,DEV=0
    HDA Intel PCH, CX20590 Analog
    Direct hardware device without any conversions
plughw:CARD=PCH,DEV=0
    HDA Intel PCH, CX20590 Analog
    Hardware device with all software conversions
sysdefault:CARD=PCH
    HDA Intel PCH, CX20590 Analog
    Default Audio Device
front:CARD=PCH,DEV=0
    HDA Intel PCH, CX20590 Analog
    Front output / input
dsnoop:CARD=PCH,DEV=0
    HDA Intel PCH, CX20590 Analog
    Direct sample snooping device
hw:CARD=GoMic,DEV=0
    Samson GoMic, USB Audio
    Direct hardware device without any conversions
plughw:CARD=GoMic,DEV=0
    Samson GoMic, USB Audio
    Hardware device with all software conversions
sysdefault:CARD=GoMic
    Samson GoMic, USB Audio
    Default Audio Device
front:CARD=GoMic,DEV=0
    Samson GoMic, USB Audio
    Front output / input
dsnoop:CARD=GoMic,DEV=0
    Samson GoMic, USB Audio
    Direct sample snooping device
```                                                  

## spectrograms!

```
sox test-11025-2.wav -n spectrogram -o test-11025-2.png
```

