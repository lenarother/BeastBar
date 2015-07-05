#!/usr/bin/python3

#from game import Game

ANIMALS = {
    "1": "Skunks",
    "2": "Parrot",
    }

def enter_animal():
    for num in ANIMALS:
        print("%s\t%s" % (num, ANIMALS[num]))
    print("x\tEXIT")
    print("")
    choice = input("")
    animal = ANIMALS.get(choice, 'x')
    return animal

def print_queue(game):
    print("\nQueue status: []\n")

def game_loop():
    game = None # Game()
    #game.start()
    animal = "-"
    while animal != 'x':
        print_queue(game)
        animal = enter_animal()
        if animal != 'x':
            print ("a %s enters the queue." % animal)
            # game.add_animal(animal)
        #game.end()

