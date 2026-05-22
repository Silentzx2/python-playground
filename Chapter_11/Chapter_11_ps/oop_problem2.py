
class animals:
    @staticmethod
    def show2():
        print("oye gareeb")
class pets(animals):
    @staticmethod
    def show():
        print("aur malik kya hal hai khana wana dedo yrr ")

class dog(pets):
    @staticmethod
    def bark():
        print("baww! baww!")


d = dog
b = pets
c = animals
d.bark()
c.show2()
b.show()