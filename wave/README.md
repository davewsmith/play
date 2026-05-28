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

## spectrograms!

```
sox test-11025-2.wav -n spectrogram -o test-11025-2.png
```

