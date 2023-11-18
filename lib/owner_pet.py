class Owner:
    all_owners = []  # Class variable to store all instances

    def __init__(self, name):
        self.name = name
        self._pets = []  # List to store associated pets
        self.__class__.all_owners.append(self)  # Add instance to the list

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type")
        self._pets.append(pet)
        pet.set_owner(self)

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda x: x.name)
        return sorted_pets


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all_pets = []  # Class variable to store all instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all_pets.append(self)  # Add instance to the list

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Invalid owner type")
        self.owner = owner

