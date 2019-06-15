from abc import ABC, abstractmethod # this is getting into some object orinted design theory. May be a bit much for right now
# it will be important latter but for now just know ABC stands for Abstract Base Class. All you really need
# to know is that means there is one or more methods that are not fully defined. So an ABC class cannot
# be made into an object (in main.py dude1 and dude2 are both objects (or instances) of this class)
# so long story short, the ABC just means that you need a specalized class to make an object (see PlayerDude and CPUDude)
from attack import Attack
import random

class Dude():
    def __init__(self, attacks):
        '''that's right muliple attacks now,

        we will use attacks as a list for now. lists are special
        data structures, basically just a sequential ordered list of items
        with out going into too much detail about it thats really all you need to know'''
        self._health = 100
        self._attacks = attacks

    def executeAttack(self, attack, target):
        '''
        executes a given attack on a target

        :param attack: index into self._attacks to select which attack to use
        :param target: Dude class to hit with the attack
        '''
        # mat lab probably has something similar, but the [] are used to access element of a list. So
        # in this case ultimately, attack should be a number 0 to some other valid index of the list.
        # in programming counting start at 0 so 0 is the first element of the list, 1 is the second and so on
        self._attacks[attack].execute(target)

    @abstractmethod #another decorator like property, just defines this method as abstract. All that means is that you need to inherit and implement this method for this class to work
    def attack(self):
        raise NotImplementedError('abstact method') # it should be impossible for this method to be called (its abstract)
                                                    # if something does somehow call it, we are just throwing an error.
                                                    # Don't need to worry about that that means, just that it will crash the program

    # Quick note, a good way to think of an ABC or abstract method is an abstract method is a promise of a method.
    # to make a useable instance you must fulfil that promise.

    @property
    def health(self):
        return self._health

    def takeDamage(self, delta):
        '''This is a special kind of comment called a doc string
        its useful for documenting parameters and stuff of functions... just be aware eventually I will use them'''
        self._health -= delta
        print('health is now: {}'.format(self._health))


# as you can see PlayerDude is a specalized Dude, when it attacks it will get input from user
class PlayerDude(Dude):
    def __init__(self, attacks):
        super(PlayerDude, self).__init__(attacks)

    # this is the method we have to implement in order to create an instance of a Dude
    def attack(self, target):
        '''Something to note here, I am getting input from user, but I am not doing nearly enough saftey around checking its type
            This is just for a quick and dirty prototype, if the user were to enter a letter it would crash the program.
        '''
        # loop until we have a valid choice of attack to use
        choice = -1
        while True:
            possible_choices = list(range(0, len(self._attacks)))
            # creates a list out of range(0, length of attacks. range creates a generator (don't really need to know what that is) that can be used to get values from start to end value - 1
            # in this case start is 0 and end is length of the attacks list. So with two attacks we have 0 -> len(attacks) - 1. or 0 -> 2 -1 or 0 -> 1. If we had 4 attacks it would generate
            # 0 -> 3. Remember list indecies start at 0. So 0 is the first attack and 1 is the seccond attack etc.
            # so possible_choices ends up being a list of all possible attacks, we use that to print the possible inputs for the user and we use that to make sure we have a valid attack selected
            choice = int(input('what attack to use {}'.format(possible_choices)))
            if choice not in possible_choices: # make sure its a valid attack
                print('invalid choice, try again')
            else:
                break # while True is an infinite loop, break will break out of a loop

        self.executeAttack(choice, target)

class CPUDude(Dude):
    def __init__(self, attacks):
        super(CPUDude, self).__init__(attacks)

    def attack(self, target):
        # this line is doing serveral thing and may look confusing, but its not that bad
        # I just wrote it in one line instead of several
        # because of order of operations it first it calls len(self._attacks)
        # this returns the number of elements in the self._attacks list in this case 2
        # then we use that to all randint with the result of the len call (2) minus 1 and
        # 0. So in this case the call is randint(0, 1). We have to subract the 1 from the
        # result of len because this is being used a list index and lists start at 0
        # this gives us either a 1 or a 0 we can use to pass into the executeAttack
        self.executeAttack(random.randint(0, len(self._attacks) - 1), target)
