# Oven air pressures sensor

![](figures/overview.png)

Manufacturer: `Spartherm Feuerungstechnick`     
Type: `S-USI`    

## Description of failure
The sensor monitors the air pressure in the flue gas pipe and the pressure in the chimney room and deactivates the fan of the exhaust air heat pump in an emergency. This means that no exhaust gas is sucked into the house in poor conditions. 
Due to the fault in the power supply unit, the heat pump's fan was deactivated several times a day, forcing it to heat purely electrically. With extremely high power consumption. The error code displayed indicates a power failure.


## Failure investigation
Based on the error code, the fault is in the power supply unit. This is conventionally constructed with a transformer, bridge rectifier, capacitor and voltage regulator. As the power supply generally still works, but sometimes has dropouts, it is a good idea to start troubleshooting with the electrolytic capacitors. These only have a limited service life and are usually the first to break down. 

The capacitance and serial resistance of this component should be measured. If no measuring equipment is available, this can also be replaced on suspicion. If the device is 10 years old, this is generally not a bad idea, as it may break in the near future anyway. In this case, it is defective and will be replaced. After the repair, the appliance works perfectly again!

Component type: `100 µF`, `50 V`, `105 °C`, `RM5`     
Reichelt order number: `FR-A 100U 50`

More information on electrolytic capacitors (fault detection, replacement):      
[Tutorial capacitors](../../tutorials/capacitors/readme.md)



