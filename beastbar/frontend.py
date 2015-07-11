#!/usr/bin/python3

from game import Game, Player

ANIMALS = {
    "1": "Skunks",
    "2": "Parrot",
    "3": "Kangaroo",
    "4": "Monkey",
    "5": "Chameleon",
    "6": "Seal",
    "7": "Zebra",
    "8": "Giraffe",
    "9": "Serpent",
    "10": "Crocodile",
    "11": "Hippo",
    "12": "Lion"
    }

#TODO: Message interface

class GameTerminated(Exception): pass

class TextFrontend:

    def __init__(self):
        self.game = None

    def enter_animal(self, player):
        choices = player.get_hand_names()
        for i, animal in enumerate(choices):
            print("%s\t%s" % (i+1, animal))
        #for num in ANIMALS:
        #    print("%s\t%s" % (num, ANIMALS[num]))
        print("x\tEXIT")
        print("")
        choice = input("")
        if choice == 'x':
            self.game.end()
            raise GameTerminated("---- GAME LEFT ----")
        selected = int(choice) - 1
        animal = choices[selected] # ANIMALS.get(choice, 'x')
        return animal

    def print_queue(self):
        print("\nQueue status: []\n")

    def create_game(self):
        self.game = Game()
        self.game.add_player(Player("Kristian"))
        self.game.add_player(Player("Lena"))
        self.game.start()

    def run_game(self):
        while self.game.is_running():
            player = self.game.next_player()
            self.print_queue()
            animal = self.enter_animal(player)
            print ("a %s enters the queue." % animal)
            player.play_card(animal)

    def finalize_game(self):
        result = self.game.get_result()
        self.print_result(result)
        self.game.end()
        self.game = None

