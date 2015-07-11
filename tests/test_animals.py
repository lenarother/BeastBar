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
        self.queue_lion.extend(cards_lion)
        cards = [Skunk(), Monkey(), Zebra(), Monkey()]
        self.queue = JostlingArea()
        self.queue.extend(cards)

    def test_play_lion(self):
        lion = Lion()
        # one lion is already present so nothing should change
        new_queue = lion.enter_queue(self.queue_lion) 
	# TODO: implement
        # no lion - new lion gets first and monkeys are removed
        new_queue = lion.enter_queue(self.queue)
        self.assertEqual(len(new_queue), 3)
	self.assertTrue(new_queue[0].is_animal('Lion'))
        self.assertTrue(new_queue[1].is_animal('Skunk'))
        self.assertTrue(new_queue[2].is_animal('Zebra'))
 
        

if __name__ == '__main__':
    main()
