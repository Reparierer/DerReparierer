# Washing machine Siemens varioPerfect

![](figures/overview.png)

Manufacturer: `Siemens`    
Type: `E 14.3A varioPerfect Waschvollautomat WM14E3A3`

## Description of failure
The washing machine went out in the middle of the wash program. It then no longer turns-on.

## Failure investigation
As the washing machine no longer starts, it makes sense to first check the low voltage supply on the circuit board.
The flyback power supply unit is located in the immediate area of the selector switch. There is no output voltage. The power supply unit is therefore suspected. To be checked:
 * [check diode](../../tutorials/diodes/readme.md)
 * [check transistor](../../tutorials/mosfets/readme.md)

The transistor here is in an integrated housing that takes over the complete control of the converter (control IC). In this case, this is defective.

Furthermore, the pre-charging resistor that supplies the input capacitor of the flyback is burnt out.

Replacing the control IC and the pre-charging resistor rectifies the fault. The power supply runs again. 

Reichelt numbers:    
Control-IC: `TNY264GN`    
Resistor `10 Ohm`, `3 W`: `VIT CR254R10`

It is also advisable to replace the output capacitor. These components only have a limited service life. Follow this [tutorial](../../tutorials/capacitors/readme.md) when replacing the electrolytic capacitor.