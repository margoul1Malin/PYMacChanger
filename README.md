# PYMacChanger
Simple Python MAC Address Changer

![readmegithub](https://github.com/user-attachments/assets/2540f990-0555-4fb7-8544-b67a89d7327d)

## Get Program : 

git clone https://github.com/margoul1Malin/PYMacChanger.git

## Adding Requirements

```python 
pip install requirements.txt  
```

## Usage:

The next command will show you available interfaces and display help message:

```python 
python3 MAC_Changer.py  
```
Once you know your interfaces

```python 
python3 MAC_Changer.py -i interface_name #Where interface_name is eth0 or wlan0 in most cases
```

The above command will generate a random MAC Address but you can also choose the new MAC by typing:

```python 
python3 MAC_Changer.py -i interface_name -m AA:BB:CC:DD:EE:FF
```



> [!NOTE]
> This Program is designed for Unicast MAC Addresses if you need informations about other types send a message :)
