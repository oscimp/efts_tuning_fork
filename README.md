# European Frequency and Time Seminar (EFTS) quartz tuning fork laboratory session.

A quartz tuning fork packaged in a transparent casing is used to demonstrate
* closed loop oscillation using a Negative Impedance Converter (NIC) circuit
* openloop stroboscopic imaging of the quartz prong motion driven by sound card output.

<a href=kicad/>KiCAD</a> board design files.

<img src="stroboscopy/tuning_fork.gif">

## References:

### Hardware
* 32768 Hz tuning fork in transparent package:
* sound card <a href="https://www.amazon.fr/-/en/UGREEN-External-Headphones-Compatible-Raspberry/dp/B08Y8CZB2S/">UGREEN (10.2 euros on amazon)</a>

### Software
* use ``mplayer tv://`` to display the webcam output since ``vlc`` does not seem to
display properly on the Raspberry Pi 5
* GNU Radio <a href="stroboscopy/snd.grc">flowchart</a> for driving the two channels of the
stereo sound card.
