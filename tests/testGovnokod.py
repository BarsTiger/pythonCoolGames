i = 1
print(10-i)

i = "meow"
print(i)

i = True
print(i)

i = ["meow", 1, True]
print(i)

i = {"cat": 1, "meow": 2, True: False}
print(i)
print(i["cat"])
print(i[True])

i = (3, 5)
print(i)
print(i[1], i[0])

class Cat(object):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print("meow")

class Dog(object):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print("bark")

class Animal:
    def __init__(self):
        pass
    def voice(self):
        print("Abstract RRRR!")

i = Cat("Barsik")
i.voice()

i = Dog("Sharik")
i.voice()

i = Animal()
i.voice()

# list = [1, 2, 3]
# print(list)
# i, c, f = 1, 2, 3