import os, subprocess, random as r, optparse, sys
import netifaces, re


######### ARGUMENT PARSER AND HELP DISPLAY
parser = optparse.OptionParser()
parser.add_option('-i', '--interface', dest="interface", help="Interface to change MAC. It Can be wlan0 or eth0 in most cases.")
parser.add_option('-m', '--mac', dest="userMac", help="Add the New MAC Address.")
(options, arguments) = parser.parse_args()


######### CHECK IF INTERFACE OPTION IS TYPED
if options.interface is None:
    
    print('\n \033[91mMAC_Changer needs an interface to work, use -i !\033[0m \n')
    
    parser.print_help()

    print('\n \033[91mYour availables interfaces are : \033[0m \n')
    for x in netifaces.interfaces():
        if x == "eth0" or x == "wlan0":
            print(f"- {x}")
            print(f'\033[0;32mCommand should be : python3 MAC_Changer.py -i {x}\033[0;32m')

    sys.exit(1)

    

######### PARSER OPTIONS USER
interface = options.interface
userMac = options.userMac


######### CHANGE MAC USUALLY
def changeMac():

    alphabet = 'abcdef'
    alphabet = list(alphabet)

    number = '123456789'
    number_Even_Unicast = '2468'
    number = list(number)
    number_Even_Unicast = list(number_Even_Unicast)

    L = r.choice(number_Even_Unicast)
    N = r.choice(number_Even_Unicast)

    phrase = [f"{L}{N}:"] 

    i = 1

    while i < 6:
        i+=1
        newnumber = r.choice(number)
        newalpha = r.choice(alphabet)
        if i == 6:
            phrase.append(f'{newnumber}{newalpha}')
        else:
            phrase.append(f'{newnumber}{newalpha}:')

    newMac = "".join(phrase)    

    if options.userMac is None:
        subprocess.call(f'ifconfig {interface} down', shell=True)
        subprocess.call(f'ifconfig {interface} hw ether {newMac}', shell=True)
        subprocess.call(f'ifconfig {interface} up', shell=True)
        chk_opt = subprocess.check_output(['ifconfig', options.interface])
        regex_opt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(chk_opt))
        if regex_opt:
            print(f"New Mac = {str(regex_opt.group(0))}")
        else:
            print('[-] Couldn\'nt read MAC Address')
    else:
        subprocess.call(f'ifconfig {interface} down', shell=True)
        subprocess.call(f'ifconfig {interface} hw ether {userMac}', shell=True)
        subprocess.call(f'ifconfig {interface} up', shell=True)
        
        chk_opt = subprocess.check_output(['ifconfig', options.interface])
        regex_opt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(chk_opt))
        if regex_opt:
            print(f"New Mac = {str(regex_opt.group(0))}")
        else:
            print('[-] Couldn\'nt read MAC Address')



######### CHANGE MAC PERMANENTLY
def changeMacPerm():

    alphabet = 'abcdef'
    alphabet = list(alphabet)

    number = '123456789'
    number_Even_Unicast = '2468'
    number = list(number)
    number_Even_Unicast = list(number_Even_Unicast)

    L = r.choice(number_Even_Unicast)
    N = r.choice(number_Even_Unicast)

    phrase = [f"{L}{N}:"] 

    i = 1

    while i < 6:
        i+=1
        newnumber = r.choice(number)
        newalpha = r.choice(alphabet)
        
        if i == 6:    
            phrase.append(f'{newnumber}{newalpha}')
        else:
            phrase.append(f'{newnumber}{newalpha}:')

    newMac = "".join(phrase)

    print('Done !')

    if options.userMac is None:
        print('Changing MAC Permanently...')
        subprocess.call(f'ip link set {interface} down', shell=True)
        subprocess.call(f'ip link set {interface} address {newMac}', shell=True)
        subprocess.call(f'ip link set {interface} up', shell=True)
        chk_opt = subprocess.check_output(['ifconfig', options.interface])
        regex_opt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(chk_opt))
        if regex_opt:
            print(f"New Mac = {str(regex_opt.group(0))}")
        else:
            print('[-] Couldn\'nt read MAC Address')

    else:
        print('Changing MAC Permanently...')
        subprocess.call(f'ip link set {interface} down', shell=True)
        subprocess.call(f'ip link set {interface} address {userMac}', shell=True)
        subprocess.call(f'ip link set {interface} up', shell=True)
        
        chk_opt = subprocess.check_output(['ifconfig', options.interface])
        regex_opt = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(chk_opt))
        if regex_opt:
            print(f"New Mac = {str(regex_opt.group(0))}")
        else:
            print('[-] Couldn\'nt read MAC Address')


######### CHECK IF USER IS ROOT
if os.geteuid() != 0:
    exit("YOU MUST BE ROOT TO USE IT ! QUITING !!!")


######### MAIN FUNCTION
def Query():
    
    userIpt = input('Want to change usually or permanently ? 1 or 2 : ')

    if userIpt == "1":
        changeMac()
    elif userIpt == "2":
        print('Copying your real MAC to real_mac_addr.txt')
        subprocess.call("ip link show eth0 | grep permaddr | awk '{print $6}' > real_mac_addr.txt", shell = True)
        changeMacPerm()
    else:
        print('1 OR 2 IS IT COMPLICATE TO UNDERSTAND ????!!!!')


Query()