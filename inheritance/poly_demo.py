import animals

def main():
    mammal = animals.Mammal('Regular Animal')
    dog = animals.Dog()
    cat = animals.Cat()

    print('Animals and the sound they make')
    print('-----------------------------')
    show_mammal_info(mammal)
    print()
    show_mammal_info(dog)
    print()
    show_mammal_info(cat)
    print()
    show_mammal_info('I am a string')


def show_mammal_info(creature):
    if isinstance(creature, animals.Mammal):
        creature.show_species()
        creature.make_sound()
    else:
        print('That is not an animal')

main()
