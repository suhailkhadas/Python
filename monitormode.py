import subprocess

subprocess.call(["iwconfig"])

def mon_mode(interface, mode):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["iwconfig", interface, "mode", mode])

    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["iwconfig"])

interface=input("Enter the Name of Interface: ")
mode=input("Enter the Mode Managed or Monitor: ")

mon_mode(interface,mode)
    
