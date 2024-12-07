# Incorrect system time of heating system 



Manufacturer: `Buderus`    
Type: `Loganagas G_124 Lownox `

## Description of failure
The system time seems to be not set proper. The rythm between day and night (colder during the night) seems to be shifted.

## Failure investigation
The timer element of the heater has an internal battery. It is a NiCd battery with a voltage of `2.3 V`. A new battery has a voltage about `3.6 V`, so this one is empty and needs to be replaced. It is soldered on the PCB and can be replaced using a soldering iron. After replacing the battery with a new one, date and time must be set, and the heating system work as usual again. 

Reichelt order number: `LS 14500CNA`
Size: `AA`
Capacity: `2600 mAh`
