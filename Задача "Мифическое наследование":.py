class Hourse:
    def __init__(self):
        self.x_distance = 0                    #пройденный путь.
        self.sound = 'Frrr'                    #звук, который издаёт лошадь.
        super().__init__()
    def run(self, dx):
        self.x_distance += dx                  # увеличивает путь на dx


class Eagle:
    def __init__(self):
        self.y_distance = 0                             #высота полёта
        self. sound = 'I train, eat, sleep, and repeat'  #звук, который издаёт орёл

    def fly(self, dy):
        self.y_distance += dy  #изменение дистанции, увеличивает y_distance на dy.


class Pegasus(Hourse, Eagle):
    def __init__(self):
        Hourse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)   #изменения дистанции, наследование метода run
        super().fly(dy)   #изменения дистанции, наследование метода fly

    def get_pos(self):
        return self.x_distance, self.y_distance # возвращает текущее положение пегаса

    def voice(self):
        print(self.sound)  #печатает значение унаследованного атрибута sound.

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()