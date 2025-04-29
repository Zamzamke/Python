class Superhero:
    def __init__(self, name, power, strength):
        self.name = name
        self.power = power
        self.strength = strength

    def introduce(self):
        print(f"I am {self.name} and my power is {self.power}!")

    def fight(self):
        print(f"{self.name} fights using {self.power} with strength level {self.strength}!")

# Inheritance and Polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength, flight_speed):
        super().__init__(name, power, strength)
        self.flight_speed = flight_speed

    def fight(self):
        print(f"{self.name} attacks from the sky at {self.flight_speed} km/h using {self.power}!")

# Example usage
hero1 = Superhero("ThunderMan", "Electric Shock", 80)
hero2 = FlyingSuperhero("SkyQueen", "Wind Slash", 70, 300)

hero1.introduce()
hero1.fight()

hero2.introduce()
hero2.fight()


# Polymorphism in Action
class Animal:
    def move(self):
        print("This animal moves in some way.")

class Dog(Animal):
    def move(self):
        print("Dog runs on four legs. 🐶")

class Bird(Animal):
    def move(self):
        print("Bird flies in the sky. 🐦")

class Fish(Animal):
    def move(self):
        print("Fish swims in the water. 🐟")

# Demonstrating polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
