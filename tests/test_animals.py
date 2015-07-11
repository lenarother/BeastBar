from unittest import TestCase, main

from game import JostlingArea
from animals import (Monkey, Lion, 
                     Hippo, Giraffe, 
                     Zebra, Skunk, 
                     Parrot)


class AnimalTests(TestCase):

    def setUp(self):
        cards_lion = [Lion(), Monkey(), Monkey(), Hippo()]
	self.queue_lion = JostlingArea()
        self.queue_lion.cards = cards_lion
        cards = [Skunk(), Parrot(), Zebra(), Giraffe()]
        self.queue = JostlingArea()
        self.queue.cards = cards 

    def test_lion(self):
        pass
        

if __name__ == '__main__':
    main()
