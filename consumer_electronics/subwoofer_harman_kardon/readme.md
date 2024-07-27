# Subwoofer
![](figures/overview.png)

Manufacturer: `harman/kardon`    
Type: `HKTS210SUB/230`


## Description of failure
Does not turn on.

## Failure investigation
First, all supply voltages are checked for stability. To do this, the voltages across the electrolytic capacitors can be measured and checked to see if they are stable. This is not the case for the output voltage of the auxiliary power supply; the voltage across one of the capacitors is not stable. The marked capacitors `C5`, `C6`, `C26`, `C27` and `C31` (2x `220 µF`, 3x `100 µF`) are examined more closely. The following diagram shows both `220 µF` capacitors in the impedance analyzer. The lower curve shows an intact capacitor, the upper curve the broken one. The latter does not exhibit a typical frequency response, but a much too high series resistance (ESR), which is greater than `10 ohms`. Normal values are well below `1 ohm`. It is recommended to replace all marked capacitors.

For capacitor investigation see also: [Capacitor tutorial](../../tutorials/capacitors/readme.md)

![](figures/impedance_capacitors_220uF.png)

Furthermore, a visual inspection of the power supply reveals that the snubber resistor of the flyback has faded due to the heat generated. This is easily damaged and should be replaced. It is a `51 Ohm` resistor with `1 W`. Due to the high heat exposure, a `1 W` resistor does not seem to be enough and should therefore be replaced by a `2 W` resistor.

