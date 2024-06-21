# class Animal:
#     def habitat(self):
#         print("habitat: I live outside as Wild or pet animal")
#
# class Dog(Animal):
#     def __init__(self):
#         print("I'm a dog")
#         self.pet: True
#         self.grown: True
#
#     def grown(self):
#         self.habitat()
#         print("grown: I'm mostly grown as pet and I also stay outside")
#
# d = Dog()
# d.grown()
#
# print(isinstance(d,Animal))
# print(issubclass(Dog,Cat))

class Animal():
    def __init__(self,habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):
    def __init__(self):
        super().__init__("kennel")

    def sound(self):
        print("Woof woof!!!!")

class Lion(Animal):
    def __init__(self):
        super().__init__("jungle")

    def sound(self):
        print("Uorrr Urrr!!!!")


x = Dog()
x.print_habitat()
x.sound()

l = Lion()
l.print_habitat()
l.sound()