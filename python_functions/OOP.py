class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def print_person(self):
        print(self.name, self.age)

    @staticmethod
    def static():
        print("I am a static method")


class Employee(Person): #arv
    def __init__(self, name, age, pay):
        super().__init__(name, age)
        self.pay = pay

    def __str__(self):
        return super().__str__() + f", {self.pay}"


def main():
    person1 = Person('Anna', 34)
    person2 = Person('Pelle', 42)

    person1.email = 'anna@gmail.com'
    person1.print_person()
    person2.print_person()




if __name__ == '__main__':
    main()
