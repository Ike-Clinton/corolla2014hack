Corolla2014hack
===============
Corolla2014hack is a program designed to read, inject, and aid in reverse
engineering CAN bus messages in a 2014 Toyota Corolla S

Installing and Compiling
---------
1. `git clone https://github.com/Ike-Clinton/corolla2014hack.git`
2. `cd corolla2014hack`
3. `apt-get install libncurses5-dev`
4. `gcc -o corollahack corollahack.c -lncurses`


Usage
------

1. Either create a virtual interface with the provided script `sudo ./ make_vcan0.sh` or set up a physical interface
2. run `./corollahack [interface name]`
3. If using vcan0, use candump to dump a sample log to the virtual interface
4. If using physical can0, attach CANtact or similar supported device to
    your vehicle to start receiving frames
5. Known CAN ID values will appear at the top of the terminal
6. Received unknown frame IDs will gather at the bottom of the terminal
