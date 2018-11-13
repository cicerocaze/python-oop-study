class Dog:

    species =  'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
print("{} is {} and {} is {}". format(philo.name, philo.age, mikey.name, mikey.age))

if philo.species == "mammal":
    print("{0} is a {1}".format(philo.name, philo.species))

def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(
    get_biggest_number(philo.age, mikey.age)))
