# Lamplighter

Lamplighter is an application which illuminates your house when your phone connects with your network.

## Features

- Checks sunset times (powered by <https://sunrise-sunset.org>)
- Works with Philips Hue
- Runs in Docker
- Works on Raspberry Pi
- Support for multiple phones

## Requirements

- Wifi network
- Philips Hue lamps

## Setup

Set your preferences in `settings.json`

## install application

install pip3
> `sudo apt-get install python3-pip`

Restore packages
> `sudo pip3 install -r requirements.txt`

Install tcpdump
> `sudo apt-get install tcpdump`

### Run the application

> `sudo python3 main.py`

## docker build

Create image
> `sudo docker build -t lamplighter .`
Run image on startup
> `docker run -it --net=host --restart always lamplighter`