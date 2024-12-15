# Wi-Fi Router ZBT defective power supply

![](figures/overview.png)

Manufacturer: `zbt`     
Type: `WE1026`

## Description of failure
Does not turn on.

## Failure investigation
As no LED is lighting up, the supply voltage should be checked first. 
The input voltage of the external power supply unit is OK, a switching regulator in the device itself comes first. 
There is no voltage at its output capacitor. The control IC also looks burnt. 
This is replaced together with the output capacitor and the device works again.

Defective switch mode power supply controller: `AX3051` from `Axelite`

Note: The control IC has a ground pad. Hot-air soldering is recommended.
If only a commercially available hot air dryer is available, nearby components should be covered with aluminum foil. 
Nearby electrolytic capacitors should be desoldered beforehand, even if they are located under the aluminum foil.