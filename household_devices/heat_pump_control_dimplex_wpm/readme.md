# Heat pump control Dimplex

![](figures/overview.png)

Manufacturer: `Dimplex`    
Type: `Wärmepumpenmanager WPM`

## Description of failure
The circuit of a heat pump system is driven by a circulation pump. 
The circulation pump no longer switches on when the system is heating. 
The system is about `> 15 years` old. 

## Failure investigation
The circulation pump is controlled via a relay inside the control unit. 
This is now to be examined, as it is suspected that it has an increased on-resistance. 
The associated relay is identified by the connection of the circulation pump and desoldered. 
Now the coil can be controlled with an external `24 V DC` voltage source and the contact resistance of the normally open contact can be measured with a multimeter. 
This should be `< 1 Ohm` (measurement with multimeter), but varies from time to time and is significantly higher.

The relay is then replaced with one from another control unit. This one is left over and as good as new. 
After reassembly, the circulation pump switches on again correctly and the apartment is warm again.

In case of replacing the relay by a new one, these would fit:
Relay type: `JS-24N-K` or `Schrack RY610024`