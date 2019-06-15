from attack import Attack

class Dude():
    def __init__(self, attack): # each Dude now gets their own attack
        self._health = 100
        self._attack = attack

    def attack(self, target):
        self._attack.execute(target) # the attack class holds the logic for the attacks.
                                     # this is called encapsulation. IE only things that need to know the implementation
                                     # details know them. This also means each Dude could have two attacks and are able
                                     # to select between them and use this same method for each

    @property
    def health(self):
        return self._health

    def takeDamage(self, delta):
        '''This is a special kind of comment called a doc string
        its useful for documenting parameters and stuff of functions... just be aware eventually I will use them'''
        self._health -= delta
        print('health is now: {}'.format(self._health))

