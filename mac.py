import subprocess


subprocess.call(["ifconfig"])

def mac_changer(interface,mac_add):
    subprocess.call(["ifconfig", interface, "down"])

    subprocess.call(["ifconfig", interface, "hw", "ether", mac_add])

    subprocess.call(["ifconfig", interface, "up"])

    subprocess.call(["ifconfig"])

interface=input("Enter the Interface name: ")
mac_add=input("Enetr Mac Address:")
mac_changer(interface,mac_add)



