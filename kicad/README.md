# KiCAD schematic and board design files.

The non-plated through holes have been placed with a spacing compatible with
installing the board on top of a Raspberry Pi 4/5 single board computer for
a compact setup. Whether the heat dissipated by the processor will affect
the resonator performance remains to be demonstrated.

<img src="tuning_fork.png">

The potentiometer closest to the audio input aims at adding a DC offset to bring
the audio output within the range of the Schmitt trigger toggling voltage. Set
the sound card output to maximum amplitude to increase chances of the Schmitt 
trigger toggling. The potentiometer further from the audio input is the negative
impedance and should be tuned so that the oscillator starts (slowly !) at resonance
frequency of the tuning fork.
