class Animals:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        print(f'{self.name} is fed')

    def get_voice(self):
        print(f'{self.name} says something')

    def get_weight(self):
        print(f'{self.name} weighs {self.weight} kg')


class Goose(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        print(f'{self.goose_name} the goose is fed')

    def get_voice(self):
        print(f'{self.goose_name} the goose honks')

    def get_weight(self):
        print(f'{self.goose_name} the goose weighs {self.goose_weight} kg')

    def collect_eggs(self):
        print(f'{self.goose_name} the goose laid an egg')


class Cow(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        print(f'{self.cow_name} the cow is fed')

    def get_voice(self):
        print(f'{self.cow_name} the cow moos')

    def get_weight(self):
        print(f'{self.cow_name} the cow weighs {self.cow_weight} kg')

    def milk(self):
        print(f'{self.cow_name} the cow was milked')


class Sheep(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        print(f'{self.sheep_name} the sheep is fed')

    def get_voice(self):
        print(f'{self.sheep_name} the sheep baaas')

    def get_weight(self):
        print(f'{self.sheep_name} the sheep weighs {self.sheep_weight} kg')

    def shear(self):
        print(f'{self.sheep_name} the sheep was shorn')


class Chicken(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        print(f'{self.chicken_name} the chicken is fed')

    def get_voice(self):
        print(f'{self.chicken_name} the chicken clucks')

    def get_weight(self):
        print(f'{self.chicken_name} the chicken weighs {self.chicken_weight} kg')

    def collect_eggs(self):
        print(f'{self.chicken_name} the chicken laid an egg')


class Goat(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        print(f'{self.goat_name} the goat is fed')

    def get_voice(self):
        print(f'{self.goat_name} the goat bleats')

    def get_weight(self):
        print(f'{self.goat_name} the goat weighs {self.goat_weight} kg')

    def milk(self):
        print(f'{self.goat_name} the goat was milked')


class Duck(Animals):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def feed(self):
        print(f'{self.duck_name} the duck is fed')

    def get_voice(self):
        print(f'{self.duck_name} the duck quacks')

    def get_weight(self):
        print(f'{self.duck_name} the duck weighs {self.duck_weight} kg')

    def collect_eggs(self):
        print(f'{self.duck_name} the duck laid an egg')


def create_animal(animal_name, weight, animal_type):
    if animal_type == "goose":
        animal = Goose(animal_name, weight)
    elif animal_type == "cow":
        animal = Cow(animal_name, weight)
    elif animal_type == "sheep":
        animal = Sheep(animal_name, weight)
    elif animal_type == "chicken":
        animal = Chicken(animal_name, weight)
    elif animal_type == "goat":
        animal = Goat(animal_name, weight)
    elif animal_type == "duck":
        animal = Duck(animal_name, weight)
    else:
        raise ValueError(f"Unknown animal type: {animal_type}")

    animal.feed()

    if isinstance(animal, Goose) or isinstance(animal, Chicken) or isinstance(animal, Duck):
        animal.collect_eggs()
    if isinstance(animal, Cow) or isinstance(animal, Goat):
        animal.milk()
    if isinstance(animal, Sheep):
        animal.shear()

    return animal


animals = [
    {'name': 'Серый', 'weight': 10, 'type': 'goose'},
    {'name': 'Белый', 'weight': 12, 'type': 'goose'},
    {'name': 'Манька', 'weight': 250, 'type': 'cow'},
    {'name': 'Барашек', 'weight': 80, 'type': 'sheep'},
    {'name': 'Кудрявый', 'weight': 85, 'type': 'sheep'},
    {'name': 'Ко-Ко', 'weight': 3, 'type': 'chicken'},
    {'name': 'Кукареку', 'weight': 3.5, 'type': 'chicken'},
    {'name': 'Рога', 'weight': 45, 'type': 'goat'},
    {'name': 'Копыта', 'weight': 50, 'type': 'goat'},
    {'name': 'Кряква', 'weight': 6, 'type': 'duck'}
]

animals_instance = []
total_weight = 0

for animal in animals:
    animal_instance = create_animal(animal['name'], animal['weight'], animal['type'])
    animals_instance.append(animal_instance)
    total_weight += animal_instance.weight

print(f'Total weight of all animals: {total_weight} kg')

heaviest_animal = max(animals_instance, key=lambda x: x.weight)
print(f'Heaviest animal is {heaviest_animal.name}, weighs {heaviest_animal.weight} kg')
