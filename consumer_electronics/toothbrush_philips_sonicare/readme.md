# Toothbrush Philips Sonicare

![overview](figures/overview.jpg)

## Description of failure
 * the toothbrush does not turn on
 * charging the battery still works as usual
 * some toothbrushes do [crazy things](https://www.youtube.com/watch?v=ZQP_9Ut-olM)


## Troubleshooting
Most failures come from droplets of water entering the upper seal. This becomes leaky over time. Among other things, this corrodes the electronics inside the toothbrush. It is important to first clean the inside of the unit with isopropanol. Check and do the following things:
 * disassemble the toothbrush. There are a lot of video tutorials avaialable on the internet.
 * check the battery voltage for a charged state `> 3.9 V`. If the voltage is low, may you need to check the charging electronic. In case of `0 V` battery voltage, replace the battery.
 * direct after the batteries `+`-pole, there is a `0603` SMD fuse. Check if this fuse is fine. If you need to replace this fuse, it is not possible to double check the original value. A `2 A` type was working fine.
 * check if the `on-state` and `off-state` of the switch can be measured clearly. The Mulitmeter should show a high resistance `> 1 Mohm` for `off-state`, and a resistance `<1 Ohm` for `on-state`. If this is not the case and especially the `off-state` shows random values each time switching, replace the push button
 * mouser part number [667-EVQ-PT9A15](https://www.mouser.de/ProductDetail/Panasonic/EVQ-PT9A15?qs=8CJXEYeWfIouZ%252BtmkGWsjA%3D%3D) 

Do not forget to replace the sealing when reassembing the toothbrush. Otherwise, the failure will come again in the near future.


![disassembled_toothbrush](figures/disassembled_labeled.png)

## Additional information: Open the push button
Out of interest, the push button was disassembled. For this purpose, it was bent open with pliers, so that the inner workings are visible. The contamination of the switch inside is clearly visible. The picture was taken under the microscope.
![push_button_open](figures/push_button_open.jpg)