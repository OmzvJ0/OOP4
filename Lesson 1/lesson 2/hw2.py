# 1) Создать класс Person c атрибутами first_name, last_name
# 2) Создать доп.класс Jack и наследовать его от Person , добавив при этом дополнительные атрибуты phone_number , balance
# 3) Создать еще один класс Vito, который будет наследоваться от класса Jack :
#          у последнего класса должен быть дополнительный 1 метод:
#                  первый метод,который минусует от balance Jack n-число и плюсует это число к  Vito.balance
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Jack(Person):
    current_balance = 0
    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name,)
        self.phone_number = phone_number
        self.balance = balance


class Vito(Jack):
    current_balance1 = 10

    def __init__(self, first_name, last_name, phone_number, balance,):
        super().__init__(first_name, last_name, phone_number, balance)



    def vito_balance(self):
        raznica = Jack.balance - self.current_balance1
        sum = Vito.balance + raznica
        print(f" Сумма равна: {sum}")



Jack = Jack("Jack", "Stone", "07754545", 10000)
Vito = Vito("Vito", "Stonel", "088888", 5000)
Vito.vito_balance()
