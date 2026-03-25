from pyscript import display, document

class Dog:
    def __init__(self, name, age, color, breed):
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

        # create a method



def dog(e):
    class Dog:
        def __init__(self, name, age, color, breed):
            self.name = name
            self.age = age
            self.color = color
            self.breed = breed


        def bark(self):
            display('Bark'*5, target='output5')

    name = document.getElementById('input1').value
    age = int(document.getElementById('input2').value)
    color = document.getElementById('input3').value
    breed = document.getElementById('input4').value

    dog1 = Dog('Luna', 1, 'black', 'German Shepherd')
    dog2 = Dog('Ollie', 7, 'white', 'Maltese Shih tzu')
    dog3 = Dog(name, age, color, breed)
    dog4 = Dog('Clint', 4, 'brown', 'French Bulldog')

    display(f'The name of the dog is {dog1.name}. The age of the dog is {dog1.age}. The color of the dog is {dog1.color}. The breed is {dog1.breed}', target='output5')
    display(f'The name of the dog is {dog2.name}. The age of the dog is {dog2.age}. The color of the dog is {dog2.color}. The breed is {dog2.breed}', target='output5')
    display(f'The name of the dog is {dog3.name}. The age of the dog is {dog3.age}. The color of the dog is {dog3.color}. The breed is {dog3.breed}', target='output5')
    display(f'The name of the dog is {dog4.name}. The age of the dog is {dog4.age}. The color of the dog is {dog4.color}. The breed is {dog4.breed}', target='output5')
