class Vehicle:

    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str) -> None:
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color


    __COLOR_VARIANTS = ['gray', 'red', 'yellow', 'black', 'blue', 'orange']

    def get_model(self, __model):
        return f'Модель {self.__model} '

    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя {self.__engine_power} л.с. '

    def get_color(self, __color):
        return f'Цвет {self.__color} '

    def print_info(self):
        print(f'{self.get_model(self)}\n{self.get_horsepower(self)}\n{self.get_color(self)}\nВладелец {self.owner}')

    def set_color(self, new_color: str) -> str:
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
            return self.__color
        else:
            print(f'Нельзя сменить цвет на {new_color}')



class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5


veh1 = Sedan('John', 'Subaru', 175, 'gray')

veh1.print_info()
veh1.set_color('Pink')
veh1.set_color('BLACK')
veh1.owner = 'Anastasia'
veh1.print_info()



