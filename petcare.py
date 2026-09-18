class Pet:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.__health = 100

    def get_health(self):
        return self.__health

    def set_health(self, value):
        if 0 <= value <= 100:
            self.__health = value
        elif value < 0:
            self.__health = 0
        else:
            self.__health = 100

    def make_sound(self):
        return "Some generic pet sound"

    def perform_checkup(self):
        return f"{self.name} is getting a routine checkup."


class Dog(Pet):
    def __init__(self, name, breed, favorite_toy):
        super().__init__(name, breed)
        self.favorite_toy = favorite_toy

    def make_sound(self):
        return "Woof! Woof!"

    def perform_checkup(self):
        current_health = self.get_health()
        self.set_health(current_health - 5)
        return f"Checking {self.name} the Dog's tail and paws. Energy spent!"


class Cat(Pet):
    def __init__(self, name, breed, indoor_only=True):
        super().__init__(name, breed)
        self.indoor_only = indoor_only

    def make_sound(self):
        return "Meow~"

    def perform_checkup(self):
        current_health = self.get_health()
        self.set_health(current_health + 10)
        return f"Grooming {self.name} the Cat and checking whiskers. Health boosted!"


class Bird(Pet):
    def __init__(self, name, breed, can_fly=True):
        super().__init__(name, breed)
        self.can_fly = can_fly

    def make_sound(self):
        return "Chirp! Chirp!"

    def perform_checkup(self):
        return f"Checking {self.name} the Bird's feathers and beak."


def display_dashboard(pet_list):
    print("--- MY PET CARE DASHBOARD ---")
    for pet in pet_list:
        print(f"Name: {pet.name} | Breed: {pet.breed}")
        print(f"Sound: {pet.make_sound()}")
        print(f"Action: {pet.perform_checkup()}")
        print(f"Current Health Status: {pet.get_health()}/100")
        print("-" * 30)


my_pets = [
    Dog("Buddy", "Golden Retriever", "Tennis Ball"),
    Cat("Whiskers", "Siamese", True),
    Bird("Pip", "Parakeet", True)
]

my_pets[0].set_health(90)
my_pets[1].set_health(80)

display_dashboard(my_pets)
