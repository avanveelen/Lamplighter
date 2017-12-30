from sunset import Sunset
from hue_light import Hue

class Lamplighter:

    def update(self, message):
        print('{} got message "{}"'.format('Lamplighter', message))
        self.__illuminate()

    def __illuminate(self):
        sunset = Sunset()

        if sunset.is_the_sun_set():
            print("Sun is set, turn on lights.")
            huelight = Hue()
            huelight.turn_lights_on()
        else:
            print("Sun is up, do not turn on lights.")
