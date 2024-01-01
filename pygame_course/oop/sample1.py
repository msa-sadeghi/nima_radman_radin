class Dog:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def eat(self):
        if self.gender == "boy":
            print(f"{self.name}, Good Boy EatUp")

        else:
            print(f"{self.name}, Good Girl EatUp")
    def bark(self):
        print("WOOF WOOF WOOF")


class Beagle(Dog):
    def __init__(self, name, age, gender, gunshy):
        super().__init__(name, age, gender)
        self.gunshy = gunshy

    def hunt(self):
        print("Hunt")

beagle_1 = Beagle("beagle_1", 11, "boy")
beagle_1.eat()




# dog_1 = Dog("jessi", 3, "girl")
# dog_1.eat()
# dog_2 = Dog("peter", 5, "boy")
# dog_2.eat()