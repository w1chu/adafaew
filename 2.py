class Grandparent:
    height = 170
    satiety = 100
    def __init__(self):
        age = 60

class Parent(Grandparent):
    def __init__(self):
        age = 40
        super().__init__(self.age)

class Child(Parent):
    height = 95

    def __init__(self):
        super().about()
        super().about_myself()

# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#
#     def __init__(self):
#         self.world = "world"
#         self._world = "_world"
#         self.__world = "__world"
#
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class Hi(Hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self._hello)
#         #print(self.__hello)
#         print(self.world)
#         print(self._world)
#         #print(self.__world)
# hello = Hello_world()
# hello.printer()
#
# hi = Hi()
# hi.hi_print()