import sys
import os


def getMacAddress_method1():
    """
    prints all mac addresses from system
    :return: mac address
    """
    ls = []
    if sys.platform == 'win32':
        for line in os.popen("ipconfig /all"):
            if line.lstrip().startswith('Physical Address'):
                mac = line.split(':')[1].strip().replace('-', ':')
                ls.append(mac)
                return ls
                # print(mac)
    else:
        for line in os.popen("/sbin/ifconfig"):
            if line.find('Ether') > -1:
                mac = line.split()[4]
                break
    return mac


def getMacAddress_method2():
    list = []
    if sys.platform == 'win32':
        for line in os.popen("wmic csproduct get UUID"):
            if len(line.strip()) > 1:
                l = "".join(line.split())
                if len(l) > 4:
                    print(l)


def getMacAddress_method3():
    """
    
    :return: mac address 
    """
    import uuid
    # mac = hex(get_mac())[2:].upper()
    # mac = ':'.join(mac[i:i+2] for i in range(0,len(mac),2))
    mac = uuid.getnode()
    mac = ':'.join(("%012X" % mac)[i:i + 2] for i in range(0, 12, 2))
    return mac


def getMacAddress_method4():
    """
    
    :return: mac address with description 
    """
    import wmi
    c = wmi.WMI()
    for interface in c.Win32_NetworkAdapterConfiguration():
        if interface.MACAddress:
            if 'virtual' not in interface.Description.lower():
                print(interface.Description, interface.MACAddress, interface.databasepath, sep=' : ')
                return "{} : {} : {}".format(interface.Description, interface.MACAddress, interface.databasepath)


def getMacAddress_method5():
    """
    
    :return: mac address 
    """
    import subprocess
    power_shell_path = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    res = subprocess.Popen([power_shell_path, "Get-CimInstance win32_networkadapterconfiguration"]).read().strip()
    return "{}".format(res)


# subprocess.call([power_shell_path, "Get-CimInstance win32_networkadapterconfiguration | select description, macaddress | where {$_.MACAddress -ne $null}"])

def getDiskSerialNumber():
    """
    
    :return: hdd serial number 
    """
    import wmi
    c = wmi.WMI()
    for disk in c.Win32_LogicalDisk():
        print(disk.Caption, disk.Description, disk.ProviderName)
        return disk.Caption, disk.Description, disk.ProviderName


print(getMacAddress_method5())

########################################################################################################################
# powershell command                                                                                                   
#                                                                                                                      
# Get-CimInstance win32_networkadapterconfiguration | select description, macaddress | where {$_.MACAddress -ne $null}
#                                                                                                                      
########################################################################################################################
