Corolla2014hack
===============
Corolla2014hack is a program designed to read, inject, and aid in reverse
engineering CAN bus messages in a 2014 Toyota Corolla S

Usage
------

1 - Either create a virtual interface with the provided script or set up a physical interface
2 - run ./corollahack [interface name]
3 - If using vcan0, use candump to dump a sample log to the virtual interface
4 - If using physical can0, attach CANtact or similar supported device to
    your vehicle to start receiving frames
4 - Known CAN ID values will appear at the top of the terminal
5 - Received unknown frame IDs will gather at the bottom of the terminal
