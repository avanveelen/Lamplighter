import json
import requests

class Hue:
    """Philips Hue class to turn lights on or off."""

    hue_ip_address = '192.168.1.104'
    username = 'wbA0TTIXWE7ZsrQ888HifWTXoGAEdZFeT0ZpXHQs'
    base_url = 'http://' + hue_ip_address + '/api/' + username
    
    def turn_lights_on(self):
        """Turns on the light of a group"""
        
        if self.__are_lights_on():
            print("Lights are already on.")
            self.__alert()
        else:
            url =  self.base_url + '/groups/1/action'
            data = '''{"on":true, "sat":254, "bri":200, "transitiontime":30}'''
            requests.put(url, data=data)

    def turn_lights_off(self):
        """Turns off the light of a group"""
        url = self.base_url + '/groups/1/action'
        data = '''{"on":false}'''
        requests.put(url, data=data)

    def __are_lights_on(self):
        url = self.base_url + '/groups/1'
        result = requests.get(url)
        data = json.loads(result.content.decode('utf-8'))
        return data['state']['any_on']

    def __alert(self):
        url = self.base_url + '/groups/1/action'
        data = '''{"alert" : "select" }'''
        requests.put(url, data=data)
        