class Animal:
    pass

class Skunk(Animal):
    """
    A skunk expels all animals of the two stronegest
    currently displayed species, but never other skunks.
    """
    pass

class Parrot(Animal):
    """
    A parrot shoos out an animal of your choice.
    """
    pass

class Kangaroo(Animal):
    """
    A kangaroo jumps over up to two animals.
    The strength of jumped over animals does not matter.
    """
    pass

class Monkey(Animal):
    """
    A single monkey has no effect.
    If there are more than one monkey, hippos and
    crocodiles get expeled. The last played monkey is placed
    first, the other monkes go to the position 2, 3, and 4 
    in the reverse order.
    """
    pass

class Chameleon(Animal):
    """
    A chameleon carries out the action of a species that is
    present in the queue. For this action chameleon takes on
    the strength of the imitated species.
    During execution of recurring actions chameleon is 
    chameleon again.  
    """
    pass

class Seal(Animal):
    """
    swaps the party entrance and the end of the queue.
    Effectively, the entire queue is reversed.
    """
    pass

class Zebra(Animal):
    """
    Is protected from crocodiles. Can't be overtaken 
    by crocodiles and/or hippos.
    """
    pass

class Giraffe(Animal):
    """
    Overtakes a weaker animal in front of it (recurring).
    """
    pass 

class Snake(Animal):
    """
    Sorts the entire queue by numbers.
    """
    pass

class Crocodile(Animal):
    """
    Eats all animals with lower values in front of it (recurring).
    Does not eat zebras.
    """
    pass

class Hippo(Animal):
    """
    Skips all animals with lower numbers in front of it (recurring).
    Does not skip zebras.
    """
    pass

class Lion(Animal):
    """
    Kicks out all monkeys and goes to the front of the queue.
    Immediately is discarded if there already is a lion.
    """
    pass
