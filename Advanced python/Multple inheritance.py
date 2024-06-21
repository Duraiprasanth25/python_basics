# class Father():
#     def skills(self):
#         print("Drawing,Reading")
#
# class Mother():
#     def skills(self):
#         print("Cooking,Dancing")
#
# class Brother():
#     def skills(self):
#         print("Skating,Playing")
#
# class Child():
#     def skills(self):
#         Father.skills(self)
#         Mother.skills(self)
#         Brother.skills(self)
#         print("Studying,Coding")
#
# c = Child()
# c.skills()


class Teacher():
    def teachers_action(self):
        print('I can teach')

class Student():
    def students_action(self):
        print('I can code')

class Youtuber():
    def youtubers_action(self):
        print('I can teach and code')

class Person(Teacher,Student,Youtuber):
    pass

c = Person()
c.teachers_action()
c.students_action()
c.youtubers_action()


