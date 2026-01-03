class Device:
    def turn_on(self):
        pass

class TV(Device):
    def turn_on(self):
        return "Телевизор включен"

class Radio(Device):
    def turn_on(self):
        return "Радио включено"

class Remote:
    def __init__(self, device):
        self.device = device
    
    def power_on(self):
        return self.device.turn_on()

if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    remote = Remote(tv)
    print(remote.power_on())

    remote = Remote(radio)
    print(remote.power_on())
