import abc


class Device(abc.ABC):
    @abc.abstractmethod
    def power_on(self):
        """Power on the device in a way specific to the type of device."""
        pass

    @abc.abstractmethod
    def power_off(self):
        """Power off the device."""
        print("Device is shutting down")


class Computer(Device):
    def power_on(self):
        print("Computer starting up...")
        super().power_on()

    def power_off(self):
        print("Computer shutting down...")
        super().power_off()

    def boot_up(self):
        print("Operating system booting up")


class Laptop(Computer):
    def power_on(self):
        print("Laptop powering on with quick boot")
        super().power_on()

    def power_off(self):
        print("Laptop going into hibernation")
        super().power_off()

    def open_lid(self):
        print("Laptop lid opened")


class Smartphone(Computer):
    def power_on(self):
        print("Smartphone lighting up screen")
        super().power_on()

    def power_off(self):
        print("Smartphone locking screen")
        super().power_off()

    def swipe_unlock(self):
        print("Smartphone unlocked with swipe")


class Tablet(Smartphone):
    def power_on(self):
        print("Tablet powering on with battery optimization")
        super().power_on()

    def touch_screen(self, action):
        print(f"Tablet registered a {action} on the touchscreen")


class Wearable(Device):
    def power_on(self):
        print("Wearable device waking up")

    def power_off(self):
        print("Wearable device going to sleep")


class SmartWatch(Wearable):
    def power_on(self):
        print("SmartWatch displaying time and notifications")
        super().power_on()


class SmartGlasses(Wearable):
    def power_on(self):
        print("SmartGlasses projecting AR interface")
        super().power_on()

    def display_info(self):
        print("Displaying augmented reality information")


class HybridLaptop(Tablet, Laptop):
    def power_on(self):
        print("Hybrid Laptop/Tablet powering on with dual boot")
        Laptop.power_on(self)
        Tablet.power_on(self)

    def detach_screen(self):
        print("Screen detached to use as a standalone tablet")


def use_devices():
    devices = [
        Laptop(),
        Tablet(),
        SmartWatch(),
        SmartGlasses(),
        HybridLaptop()
    ]

    for device in devices:
        device.power_on()
        if isinstance(device, Laptop):
            device.open_lid()
        if isinstance(device, Tablet):
            device.touch_screen("tap")
        if isinstance(device, SmartGlasses):
            device.display_info()
        print("")  # Add a newline for better readability between device outputs

    for device in devices:
        device.power_off()
        print("")  # Add a newline for better readability between device outputs


if __name__ == "__main__":
    use_devices()