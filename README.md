# koteshi-san-zwei
Koteshi-san Zwei

project-notes.txt

Project name:		Koteshi-san Zwei
Author:				Matthias Koterski
Project start:		2024-02-20

Planned Features:
- Python Flask server providing web interface for GPIO interface control on Raspberry Pi
- RPi reads data from sensor (e.g. rel. humidity, temperature, air pressure) and stores it in a database
- Stored data will be visually presented on Flask web interface

Test Setup

  `.::///+:/-.        --///+//-:``    pi@delta 
 `+oooooooooooo:   `+oooooooooooo:    -------- 
  /oooo++//ooooo:  ooooo+//+ooooo.    OS: Raspbian GNU/Linux 10 (buster) armv7l 
  `+ooooooo:-:oo-  +o+::/ooooooo:     Host: Raspberry Pi 3 Model B Rev 1.2 
   `:oooooooo+``    `.oooooooo+-      Kernel: 4.19.66-v7+ 
     `:++ooo/.        :+ooo+/.`       Uptime: 32 mins 
        ...`  `.----.` ``..           Packages: 730 (dpkg) 
     .::::-``:::::::::.`-:::-`        Shell: bash 5.0.3 
    -:::-`   .:::::::-`  `-:::-       Terminal: /dev/pts/0 
   `::.  `.--.`  `` `.---.``.::`      CPU: BCM2835 (4) @ 1.200GHz 
       .::::::::`  -::::::::` `       Memory: 59MiB / 926MiB 
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
