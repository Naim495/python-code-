class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} say6 Woof |"



my_dog=Dog("Buddy","go;den retriver" )

print(my_dog.bark())