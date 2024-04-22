class Appliance:
    def turn_on(self):
        print("Appliance is turned on")

class Blender(Appliance):
    def blend(self):
        print("Blending ingredients")

class Mixer(Appliance):
    def mix(self):
        print("Mixing ingredients")

class KitchenRobot(Blender, Mixer):  # Multiple inheritance
    def cook(self):
        print("Cooking meal")

    def turn_on(self):  # Method overriding
        print("Kitchen robot is ready to assist")

def prepare_meal():
    robot = KitchenRobot()
    robot.turn_on()
    robot.blend()
    robot.mix()
    robot.cook()

if __name__ == "__main__":
    prepare_meal()
