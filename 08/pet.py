def describe_pet(animal_type, pet_name):
    """show pet info"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'engse')

def describe_pet2(animal_type, pet_name = 'hong'):
    """show pet info"""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet2('hamster')
describe_pet2('ham', 'kim')