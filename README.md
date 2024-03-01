# koteshi-san-zwei
Koteshi-san Zwei - Project Notes

Project name:     Koteshi-san Zwei
Author:           Matthias Koterski
Project start:		2024-02-20

Planned Features:
- Python Flask server providing web interface for GPIO interface control on Raspberry Pi
- RPi reads data from sensor (e.g. rel. humidity, temperature, air pressure) and stores it in a database
- Stored data will be visually presented on Flask web interface

Test Setup - 2024-02-25

  `.::///+:/-.        --///+//-:``    matthias@delta 
 `+oooooooooooo:   `+oooooooooooo:    -------------- 
  /oooo++//ooooo:  ooooo+//+ooooo.    OS: Raspbian GNU/Linux 11 (bullseye) armv 
  `+ooooooo:-:oo-  +o+::/ooooooo:     Host: Raspberry Pi 3 Model B Rev 1.2 
   `:oooooooo+``    `.oooooooo+-      Kernel: 6.1.21-v7+ 
     `:++ooo/.        :+ooo+/.`       Uptime: 1 day, 6 hours, 58 mins 
        ...`  `.----.` ``..           Packages: 1427 (dpkg) 
     .::::-``:::::::::.`-:::-`        Shell: bash 5.1.4 
    -:::-`   .:::::::-`  `-:::-       Terminal: /dev/pts/0 
   `::.  `.--.`  `` `.---.``.::`      CPU: BCM2835 (4) @ 1.200GHz 
       .::::::::`  -::::::::` `       Memory: 152MiB / 921MiB 
 .::` .:::::::::- `::::::::::``::.
-:::` ::::::::::.  ::::::::::.`:::-                           
::::  -::::::::.   `-::::::::  ::::                           
-::-   .-:::-.``....``.-::-.   -::-
 .. ``       .::::::::.     `..`..
   -:::-`   -::::::::::`  .:::::`
   :::::::` -::::::::::` :::::::.
   .:::::::  -::::::::. ::::::::
    `-:::::`   ..--.`   ::::::.
      `...`  `...--..`  `...`
            .::::::::::
             `.-::::-`


First test - LED test
Date:
2024-02-2X

Required:
- Raspberry Pi 
- LED(s)
- Resistors (ca. 330 Ohms)
- Jumper cables

Optional:
- Bread / breakout board

Description:
- LED(s) get connected to Raspberry Pi
- LED(s) can be controlled via Raspberry Pi through Python