# CD-player Pioneer X-HM11-K does not turn-on
![front](figures/front.png)


## Description of failure
The device does not start.

## Troubleshooting
![power_pcb_repair](figures/power_pcb_repair.png)

If the device does not turn on, first check the output voltage of the internal power supply unit. In this case, the output voltage of the power supply unit is `0V`. When checking the individual components of the power supply unit (flyback topology), it is noticeable that the diode has a high resistance. After replacing the diode, the device works perfectly again.

Broken diode: `MBRF20200CT`
