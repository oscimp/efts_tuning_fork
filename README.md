# <a href="https://efts.eu">European Frequency and Time Seminar (EFTS)</a> quartz tuning fork laboratory session.

A quartz tuning fork packaged in a transparent casing is used to demonstrate
* closed loop oscillation using a Negative Impedance Converter (NIC) circuit (<a href="oscillator/oscillateur_1night.png">Allan deviation</a> below $10^{-9}$ up to 30 s integration time).
* openloop stroboscopic imaging of the quartz prong motion driven by sound card output.

<a href=kicad/>KiCAD</a> board design files.

<img src="stroboscopy/tuning_fork.gif">

## References:

### Hardware
* 32768 Hz tuning fork in transparent package: <a href="https://eu.mouser.com/ProductDetail/Epson-Timing/FC-135-32.7680KA-AC5?qs=f9yNj16SXrLM6nHs1T34rQ%3D%3D">Epson FC-135 32.7680KA-AC5</a>
* sound card with sampling rate 96 kHz or higher, e.g. <a href="https://www.amazon.fr/-/en/UGREEN-External-Headphones-Compatible-Raspberry/dp/B08Y8CZB2S/">UGREEN (10.2 euros on amazon)</a>
* "digital microscope" webcam, e.g. <a href="https://amscope.co.uk/products/c-hhd510-w">AmScope HHD Series</a>
* 7414 Schmitt trigger
* 7400 NAND gate

### Software
* use ``mplayer tv://`` to display the webcam output since ``vlc`` does not seem to
display properly on the Raspberry Pi 5
* GNU Radio <a href="stroboscopy/snd.grc">flowchart</a> for driving the two channels of the
stereo sound card (tested with GNU Radio 3.10).

## Resources:

Equivalent BvD model of the quartz tuning for:
* R1=53727 $\Omega$
* L1=7221 H
* C1=3.268 fF
* C0=3.368 pF

Quality factor $Q=\frac{1}{R1}\sqrt{\frac{L1}{C1}}=27700$

Resonance frequency $f=\frac{1}{2\pi\sqrt{L1\cdot C1}}=\frac{1}{2\pi\sqrt{7221\times 3.268\cdot 10^{-15}}}=32763$ Hz

