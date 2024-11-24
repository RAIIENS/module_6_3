# module_6_3.py
# Нужно создать 5 классов:

# Создаём первый класс, это класс описывающий животных.
class Animal:
# По условию задачи класс обладает следующими атрибутами:
# live = True
# sound = None - звук (изначально отсутствует)
# _DEGREE_OF_DANGER = 0 , где 0, это минимальный уровень опасности существа
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
# Теперь объект этого класса, по условию задачи, должен обладать следующими атрибутами:
# cords = [0, 0, 0] - координаты в пространстве.
# speed = ... - скорость передвижения существа (определяется при создании объекта)
    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed
# И методами:
# move(self, dx, dy, dz), который должен менять соответствующие координаты в
# пространстве (_cords)
# на dx, dy и dz в том же порядке, что и множители в speed.
# Если при попытке изменения координаты z в _cords значение будет меньше 0,то выводить сообщение
# "It's too deep, i can't dive :(" , при этом изменения не вносить.
# далее будет выводиться следующее:
# get_cords(self) метод, который выводит координаты в формате: "X: <координаты по x>,
# Y: <координаты по y>, Z: <координаты по z>"
# attack(self) метод который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и
# "Be careful, i'm attacking you 0_0" , если равно или больше.
# speak(self) и метод который выводит строку со звуком sound.

    def move(self, dx, dy, dz):
        if self._cords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print(self.sound)

# Создаём 2 класс:
# Bird это класс описывающий птиц. Наследуется от Animal.
class Bird(Animal):
# Этот класс должен обладать атрибутом beak = True
# Это наличие клюва :=))
    beak = True
# И методом:
# lay_eggs(self), который выводит строку "Here are(is)
# <случайное число от 1 до 4> (колличество отложенных яиц) eggs for you"
    def lay_eggs(self):
# в условии задачи предлагают eggs = random.randint(1, 4)
# Мы для красоты решения задачи задаем колличество отложенных яиц равное 3
        eggs = 3
        print(f"Here are(is) {eggs} eggs for you")

# Создаём 3 класс:
# AquaticAnimal. Это класс плавающих животных. Наследуется от Animal.
class AquaticAnimal(Animal):
# По условию задачи в этом классе атрибут _DEGREE_OF_DANGER = 3.
    _DEGREE_OF_DANGER = 3
# и данный класс должен обладать методом:
# dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда
# уменьшать координату z в _coords. Чтобы сделать dz положительным, берём его значение по
# модулю (функция abs). Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии
# от обычного движения. (speed / 2). Тогда получаем следующее:
    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz
        self.speed /= 2

# Создаём 4 класс PoisonousAnimal
# Это класс описывающий ядовитых животных. Наследуется от Animal.
class PoisonousAnimal(Animal):
# В этом классе атрибут _DEGREE_OF_DANGER будет равен = 8 , т.е.максимальному показателю.
    _DEGREE_OF_DANGER = 8

# Создаём 5 класс Duckbill.
# Это класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
# Объект этого класса должен обладать одним дополнительным атрибутом:
# sound = "Click-click-click" - звук, который издаёт утконос
    def __init__(self, speed):
        super().__init__(speed)
    sound = "Click-click-click"

# Вариант примера работы программы:

db = Duckbill(10)
print(db.live)
# True
print(db.beak)
# True
db.speak()
# Click-click-click
db.attack()
# Be careful, i'm attacking you 0_0

db.move(1, 2, 3)
db.get_cords()
# X: 10 Y: 20 Z: 30

db.dive_in(6)
db.get_cords()  # X: 10 Y: 20 Z: 0

db.lay_eggs()  # Here are(is) 3 eggs for you (число может меняться)

