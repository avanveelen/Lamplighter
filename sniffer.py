import logging
import threading
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

class Sniffer:
    '''Sniffs the network on port 67 or port 68 for dhcp requests'''
    __mac_addresses = {}

    def __init__(self, mac_addresses):
        self.__mac_addresses = mac_addresses
        self.subscribers = set()
        print('Looking for: ' + str(mac_addresses))

    def register(self, who):
        '''Registers a subscriber'''
        self.subscribers.add(who)

    def unregister(self, who):
        '''Unregsiters a subscriber'''
        self.subscribers.discard(who)

    def run(self):
        '''Starts sniffing'''
        print('Start sniffing')
        sniff(filter="udp and (port 67 or port 68)",
              prn=self.__handle_dhcp, store=0)

    def __handle_dhcp(self, pkt):
        dhcp_option = pkt[scapy.layers.dhcp.DHCP].options[0][1]
        if  dhcp_option == 3:
            # pkt[BOOTP].show()
            mac = self.__get_mac_addr(pkt[scapy.layers.dhcp.BOOTP].chaddr[:6])
            # print(mac)
            if mac in self.__mac_addresses:
                print("found mac address " + mac +
                      " of " + self.__mac_addresses[mac])
                self.__dispatch(mac)
            else:
                print("unknown mac address " + mac)

    def __get_mac_addr(self, bytes_addr):
        bytes_str = map('{:02x}'.format, bytes_addr)
        return ':'.join(bytes_str).upper()

    def __dispatch(self, message):
        for subscriber in self.subscribers:
            thread = threading.Thread(target=subscriber.update(message), args=())
            thread.start()
