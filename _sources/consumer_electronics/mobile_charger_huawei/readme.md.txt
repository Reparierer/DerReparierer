# Mobile Charger

![](figures/overview.png)

Manufacturer: `HUAWEI`     
Type: `HW-050100E01`     
Output: `5 V, 1 A`

## Description of failure
Does not charge the mobile phone.

## Failure investigation
When mains voltage is applied, the voltage is tracked step by step through the power supply unit. It is noticeable that 5V voltage is measured at the first output capacitor, but there is no voltage at the second capacitor and at the USB socket.

On closer inspection, it becomes apparent that the ground line is interrupted. In this example, the earth is distributed via the housing of the USB socket (which has 4 solder connections). Due to mechanical impact on the plug over time, the conductor track has become detached from the circuit board and is broken.

The broken area is bridged with a wire and the power supply unit works perfectly again. It is also advisable to re-solder all the solder connections on the USB socket, as several of them may still be mechanically damaged.