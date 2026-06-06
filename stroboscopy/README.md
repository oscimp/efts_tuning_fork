# Experimental setup: adjusting the LED position to illuminate the tuning fork

## Preliminary tests 
<img src="IMG_20260409_120540_544.jpg">

<img src="IMG_20260409_131427_507.jpg">

## Oscilloscope screenshots: pulse driving the LED

<img src="Screenshot_2026-04-09_0_113607.png">

<img src="Screenshot_2026-04-09_1_113637.png">

## Final setup

* On the Raspberry Pi: start the graphical user interface (``startx``),
open a terminal and launch ``alsamixer`` to check the sound card setting. Using F6,
select the USB sound card and check that the volume is maximum.

* Quit ``alsamixer`` and launch ``gnuradio-companion`` with the ``snd.grc`` flowgraph.
Select a frequency around 32764 Hz (a few Hz below 32768).

* Connect SPDT SW1 pin 1 to 2 (openloop measurement by driving the
tuning fork with the sound card) and SPDT SW2 1 to 3 (75 ohm load)

<img src="IMG_20260606_140601_950.jpg">

* Adjust the voltage on pin 1 of the 7414 U2A using RV2

<img src="7414_pin1.png">

so that its output in pin 2 toggles with
a more or less 50% duty cycle:

<img src="7414_pin2.png">

* the voltage driving the LED must be a sharp negative pulse allowing the LED
to illuminate briefly the tuning fork:

<img src="led.png">
<img src="led_zoom.png">

* check that the signal driving the tuning fork reaches the pin closes to the DC-DC
switching supply:

<img src="tuning_fork_voltage.png">

* adjust the microscope position for the tuning fork picture to be centered and sharp

<img src="IMG_20260606_145209_746.jpg">

<a href="https://superuser.com/questions/556029/how-do-i-convert-a-video-to-gif-using-ffmpeg-with-reasonable-quality">Converting AVI to animated GIF</a>:

```
ffmpeg -i vlc-record-2026-05-13-09h10m45s-v4l2____dev_video0-.avi -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 vlc-record-2026-05-13-09h10m45s-v4l2____dev_video0-.gif
```

<img src="vlc-record-2026-05-13-09h10m45s-v4l2____dev_video0-.gif">
