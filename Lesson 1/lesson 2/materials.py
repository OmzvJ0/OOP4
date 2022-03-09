class Material:
    def __init__(self, polo, color, type, electric):
        self.polo = polo
        self.color = color
        self.type = type
        self.electric = electric


    def informatio(self):
        print(f"{self.electric}")


class Metall(Material):

    def __init__(self, polo, color, type, electric):
        super().__init__(polo, color, type, electric)

metal = Metall("245", "silver", "krepkii", "100")
metal.informatio()

class truba(Metall):
    def __init__(self, polo, color, type, electric):
        super().__init__(polo, color, type, electric)

class Silver(Material):

    def __init__(self, polo, color, type, electric, antibacteric):
        super().__init__(polo, color, type, electric)
        self.antibacteric = antibacteric
serebro = Silver("360", "silver", "krepkii", "50")
metal.informatio()

class ring()
def __init__(self, polo, color, type, electric):
    super().__init__(polo, color, type, electric

class Gold(Material):

    def __init__(self, polo, color, type, electric):
        super().__init__(polo, color, type, electric)

gold = Gold("500", "gold", "mygkii", "20")
metal.informatio()

class Derevo(Material):

    def __init__(self, polo, color, type, electric):
        super().__init__(polo, color, type, electric)

derevo = Derevo ("100", "grow", "krepkii", "1")
metal.informatio()

class Plastic (Material):

    def __init__(self, polo, color, type, electric):
        super().__init__(polo, color, type, electric)

plastic = Plastic ("40", "whiter", "krepkii", "20")
metal.informatio()
class asdsad: