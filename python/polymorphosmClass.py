class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("자식클래스에서 구현하시오.")
    
class Cat(Animal):
    def talk(self):
        return "야옹!"

class Dog(Animal):
    def talk(self):
        return "왈! 왈!"


def main():
    animals = [Cat('야옹이'), Dog('멍멍이'), Cat('랜시')]
    for animal in animals:
        print(animal.name + " : " + animal.talk())

if __name__ == '__main__':
    main()
