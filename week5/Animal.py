class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, age):
        self.age = age
    def set_name(self, name = ''):
        self.name = name
    def __str__(self):
        return 'Animal:' + str(self.name) + ':' + str(self.age)

class Cat(Animal):
    def speak(self):
        print('meow')
    def __str__(self):
        return 'Cat:' + str(self.name) + ':' + str(self.age)

class Rabbit(Animal):
    def speak(self):
        print('meep')
    def __str__(self):
        return 'Rabbit:' + str(self.name) + ':' + str(self.age)

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
    def __str__(self):
        return 'name:' + str(self.name) + ':' + str(self.age) + ':' + str(self.friends)

foo = Animal(3)
foo.set_name('foobar')
print(foo.get_name())

jelly = Cat(1)
jelly.speak()
jelly.set_name('jellyBelly')
print(jelly)

peter = Rabbit(1)
peter.speak()
peter.set_name('peter')
print(peter)

bob = Person('bob', 21)
print(bob)