class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        return f"{self.name} is {self.color}."

    def speak(self):
        return "Some sound"

class TransformedAnimal(Animal):
    def __init__(self, name, color, transparent_color):
        super().__init__(name, color)
        self.transparent_color = transparent_color

    def describe(self):
        return f"{self.name} is {self.color} and has been transformed to {self.transparent_color}."

class Tiger(Animal):
    def speak(self):
        return "Roar!"

class Parrot(TransformedAnimal):
    def speak(self):
        return "Squawk!"

class Elephant(Animal):
    def speak(self):
        return "Trumpet!"


def main():
    tiger = Tiger("Simba", "Golden")
    parrot = Parrot("Polly", "Green", "Blue Tint")
    elephant = Elephant("Dumbo", "Gray")

    print(tiger.describe(), "and says", tiger.speak())
    print(parrot.describe(), "and says", parrot.speak())
    print(elephant.describe(), "and says", elephant.speak())

if __name__ == "__main__":
    main()
