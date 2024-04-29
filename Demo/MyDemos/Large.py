class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def get_animal_sound(animal):
    if not isinstance(animal, Animal):
        raise ValueError("animal must be an instance of Animal")
    return animal.speak()

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class AdvancedCalculator(Calculator):
    def power(self, base, exponent):
        return base ** exponent

def example_function(x):
    if x < 0:
        return 'negative'
    elif x == 0:
        return 'zero'
    else:
        return 'positive'

if __name__ == "__main__":
    # Create instances of animals
    my_dog = Dog("Rex")
    my_cat = Cat("Whiskers")

    # Print animal sounds
    print(get_animal_sound(my_dog))
    print(get_animal_sound(my_cat))

    # Use calculator
    calc = AdvancedCalculator()
    print("3 + 5 =", calc.add(3, 5))
    print("10 - 2 =", calc.subtract(10, 2))
    print("4 * 7 =", calc.multiply(4, 7))
    print("20 / 5 =", calc.divide(20, 5))
    print("2^3 =", calc.power(2, 3))

    # Test example_function
    print("example_function(-1) returns", example_function(-1))
    print("example_function(0) returns", example_function(0))
    print("example_function(1) returns", example_function(1))
