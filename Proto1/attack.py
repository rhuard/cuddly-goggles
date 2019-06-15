import random

#this is a comment it is ignored by the python interpretor used to document stuff. I am sure matlab had them also

# this is another great exmple of using the inheritence stuff I was talking about with the animals

class Attack():
    def __init__(self, name, low, high, accuracy):
        '''
        now attacks have an accuracy to make it more interesting
        '''
        self._low = low
        self._high = high
        self._accuracy = accuracy
        self.__name__ = name

    def execute(self, target):
        # info for user
        print('Attacking with: {}'.format(self.__name__))
        # generate a random percent
        hit = random.randint(0, 100)
        print('hit score = {} accuracy = {}'.format(hit, self._accuracy))
        # if percent is less than accuracy it is a hit. This makes it easy to reason about an attack with a certain hit chance
        if hit <= self._accuracy:
            # get random number from damage range
            damage = random.randint(self._low, self._high)
            print('doing: {} damage'.format(damage))
            target.takeDamage(damage)
        else:
            print('miss')

# Here is where classes are nice... because we do not have to rewrite everything
# our attacks are all defined in 3 lines....

class Fireball(Attack):
    def __init__(self):
        super(Fireball, self).__init__('fireball', 20, 40, 30)
        # do not worry about the syntax for super.... just know
        # this is calling the parent (Attack) class's __init__.
        # you don't really need to know details of how it works and it can be complicated
        # so just know this is needed to initalize the underlying parent Attack class
        # PS parent classes are also known as superclasses. Hence the super...

class Punch(Attack):
    def __init__(self):
        super(Punch, self).__init__('punch', 5, 10, 90)

# note.... in the real game we will want these values to be read from afile
# like a text file not code, and these attack classes to be generated dynamicallly
# that way its easy to mod with out changing code. This is way more imporant
# in C++ than in python because changing code means recompiling which is not
# great for mods
