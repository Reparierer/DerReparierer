# Dryer Bosch MAXX7 sensitive does not turn-on
![overview_dryer](figures/overview.png)

Bosch MAXX7 Sensitive     
E-number: WTE843A2

## Description of failure
The dryer does not turn-on at all or turns-off automatically during usage.

## Failure investigation
The internal power supply, a flyback topology, has died. There is no stable output voltage of the flyback converter. Measuring the internal body-diode of the integrated switch shows a short.
Things to replace: 
 * Flyback controller: `TNY 266PN`
 * 2x Output capacitors `22 µF`, `105 °C`
After replacing the broken components, the dryer works totally fine.

![steps_replacing_power_supply](figures/steps.png)