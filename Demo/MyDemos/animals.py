class LifeForm:
    def respond_to_environment(self):
        print("Responding to environment")

class Animal(LifeForm):
    def eat(self):
        print("Eating")

class Plant(LifeForm):
    def photosynthesize(self):
        print("Photosynthesizing")

class Mammal(Animal):
    def breathe(self):
        print("Breathing")

class Bird(Animal):
    def fly(self):
        print("Flying")

class Dog(Mammal):
    def bark(self):
        print("Barking")

class Labrador(Dog):
    def wag_tail(self):
        print("Wagging tail")

def find_food():
    print("Finding food")

def main():
    lab = Labrador()
    lab.breathe()
    lab.eat()
    lab.bark()
    lab.wag_tail()

if __name__ == "__main__":
    main()