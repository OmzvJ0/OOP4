class Animal:
    def __init__(self,name , type, color, voiceText):
        self.name = name
        self.type = type
        self.color = color
        self.voiceText = voiceText

    def voice(self):
        print(self.voiceText)

        """Наследвание"""
class Dog(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)
class Cat(Animal):

    def __init__(self, name, type, color, voiceText):
        super().__init__(name, type, color, voiceText)

Rex = Dog(
    "Rex",
    "Domestic",
    "Blue",
    "gaf gaf"
)
Rex.voice()

Kitty = Cat('Barsik', 'Domestic', 'White', 'meow meow')
Kitty.voice()

""" Полиморфизм """

class Horse(Animal):

    def __init__(self, name, type, color, voiceText, speed, weight):
        super().__init__(name, type, color, voiceText)
        self.speed = speed
        self.weight = weight


    def voice(self):
        print(f"{self.name}: {self.voiceText}")

Mustang = Horse("Mustang", 'Domestic', "brown", 'ku ku', 30, 250)
Mustang.voiceText

"""Инкапсуляция"""




