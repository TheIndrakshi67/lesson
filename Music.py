from abc import ABC, abstractmethod

class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(self.name + " goes strum")

class Drum(Instrument):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(self.name + " goes boom")

guitar = Guitar("Guitar")
drum = Drum("Drum")

guitar.make_sound()
drum.make_sound()
