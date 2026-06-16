# Closed loop oscillator circuit

The startup time can be as long as a few minutes (hundreds of seconds).

<img src="Screenshot_2026-04-01_0_133634.png">

<img src="Screenshot_2026-04-01_1_134010.png">

The modified Allan deviation of the frequency recording over one night
exhibits a sub- $10^{-9}$ relative frequency instability up to 30 second
integration time.

<img src="oscillateur_1night.png">

## Setup

C4 was fitted with a 1 nF capacitor. In case the oscillator fails to start even at
the highest potentiometer value, remove C4.

* Close SW1 pin 2 and 3 to connect the tuning fork to the negative impedance converter circuit.

<img src="IMG_20260606_163114_419.jpg">

* Adjust RV1 until the voltage on the Oscillator output SMA jumps from -4V to 0V by decreasing
the potentiometer resistance (turning counter-clock wise).

<img src="Screenshot_2026-06-06_3_142450.png">

* Once the voltage is settled on 0V, increase the resistance (turn clock-wise) until the
oscillator starts.

<img src="Screenshot_2026-06-06_4_142516.png">

<img src="Screenshot_2026-06-06_5_142603.png">

In the following test (operational amplifier output connected to 50 ohms oscilloscope
channel) the oscillator returned to the -4V fixed value:

<img src="Screenshot_2026-06-06_2_141429.png">

