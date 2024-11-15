# PYMacChanger
Simple Python MAC Address Changer

Get Program : https://github.com/margoul1Malin/PYMacChanger.git

Usage:

The next command will show you available interfaces and display help message:

python3 MAC_Changer.py   

Once you know your interfaces

python3 MAC_Changer.py -i interface_name <- Where interface_name is eth0 or wlan0 in most cases

The above command will generate a random MAC Address but you can also choose the new MAC by typing:

python3 MAC_Changer.py -i interface_name -m AA:BB:CC:DD:EE:FF



