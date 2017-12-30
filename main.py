from sniffer import Sniffer
from lamplighter import Lamplighter

def main():
    '''Main of the application'''

    print("Starting application...")
    mac_addresses = {
        'F4:F5:24:D8:82:15': 'Alexander',
        '68:FB:7E:38:6C:3B': 'Ylona'
    }

    sniffer = Sniffer(mac_addresses)
    lamplighter = Lamplighter()
    sniffer.register(lamplighter)
    sniffer.run()
    
main()
