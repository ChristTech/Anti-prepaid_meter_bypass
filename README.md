# Anti-prepaid_meter_bypass
A software simulation of an anti prepaid meter bypass, to reduce energy theft

 Goal: Build a software that detects when a prepaid meter is bypassed.

Rough Plan:
    To check if the wires are connected to the prepaid meter, the meter is charged a certain amount of units (made possible by an on-board circuitry)
which is returned immediately after verification (this will be done multiple times continously). if the verification is unsuccessful then:
    1. the software will alert the system admin of a suspected by-pass
    2. send the address of the user who has been suspected of the by-pass.

problems with this system:
1. What happens when there's no unit left in the meter? wouldn't that give a false alert?

solution
1. There should be a fixed amount of unit that will be allocated to each prepaid, this unit will only be used for the verification process not for 
   supply of electricity to the customer 
