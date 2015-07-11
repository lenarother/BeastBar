#!/usr/bin/python3

from game import Game, Player

ANIMALS = {
    "1": "Skunks",
    "2": "Parrot",
    }

#TODO: Message interface

class TextFrontend:

    def __init__(self):
        self.game = None

    def enter_animal(self, player):
        for num in ANIMALS:
            print("%s\t%s" % (num, ANIMALS[num]))
        print("x\tEXIT")
        print("")
        choice = input("")
        animal = ANIMALS.get(choice, 'x')
        #TODO: raise exception for x
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
            if animal == 'x':
                exit()
            print ("a %s enters the queue." % animal)
            player.play_card(animal)

    def finalize_game(self):
        result = self.game.get_result()
        self.print_result(result)
        self.game.end()
        self.game = None

