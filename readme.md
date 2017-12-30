# DHCP sniffer + Philipes Hue

## install application

install pip3
> `sudo apt-get install python3-pip`

Restore packages
> `sudo pip3 install -r requirements.txt`

Install tcpdump
> `sudo apt-get install tcpdump`

## Run the application

> `sudo python3 sniffer2.py`

## docker build

> `sudo docker build -t sniffer .`
> `docker run -it --net=host --restart always sniffer`