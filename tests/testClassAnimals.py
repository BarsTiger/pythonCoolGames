class Animal(object):
    def __init__(self):
        pass

    def voice(self):
        pass

    def move(self):
        pass
    def size(self, weight, length):
        self.weight = weight
        self.length = length

    def age(self, age):
        self.age = age

class Mammal(Animal):
    def __init__(self):
        pass
    def move(self):
        print("run")

class Fish(Animal):
    def __init__(self):
        super(self)

    def voice(self):
        print(".......")

    def move(self):
        print("swim")

class Bird(Animal):
    def __init__(self):
        super(self)

    def move(self):
        print("fly")


class Cat(Mammal):
    def __init__(self, name):
        self.name = name

    def voice(self):
        print("meow")


class Dog(Mammal):
    def __init__(self, name):
        self.name = name
    def voice(self):
        print("bark")


class Platypuss(Mammal):
    def __init__(self, name):
        self.name = name
    def move(self):
        print("run, swim")
    def voice(self):
        print("RRRRRRRRRR")


class Duck(Bird):
    def __init__(self):
        pass
    def voice(self):
        print("kraaaa")
    def move(self):
        print("fly, swim")

class Penguin(Bird):
    def __init__(self):
        pass

    def voice(self):
        print("ar")

    def move(self):
        print("go, swim")

class Shark(Fish):
    def __init__(self):
        pass

class Flyfish(Fish):
    def __init__(self):
        pass
    def move(self):
        print("swim, fly")

cat = Cat("Barsik")
dog = Dog("Sharik")
platypuss = Platypuss("Perry")
duck = Duck()
penguin = Penguin()
shark = Shark()
flyfish = Flyfish()

print("cat")
cat.voice()
cat.move()

print("dog")
dog.voice()
dog.move()

print("platypuss")
platypuss.voice()
platypuss.move()

print("duck")
duck.voice()
duck.move()

print("penguin")
penguin.voice()
penguin.move()

print("shark")
shark.voice()
shark.move()

print("flyfish")
flyfish.voice()
flyfish.move()

