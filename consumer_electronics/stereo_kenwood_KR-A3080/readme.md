# Stereo KENWOOD
![](figures/overview.png)

Manufacturer: `KENWOOD`    
Type: `KR-A3080`

## Description of failure
The stored radio stations are lost after switching off and on.

## Failure investigation
The radio contains a supercap, which is responsible for the station memory. This is a `5.5V 47mF` type, which is defective. A `47mF` replacement type could not be found in the right size, but a larger one with `100mF` (`Korchip DCS5R5104HF`). A supercap with more capacity is not a problem here. After replacing the component, the radio stations are still present after switching off and on. 