import random

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

class Fireball(Attack):
    def __init__(self):
        super(Fireball, self).__init__('fireball', 20, 40, 30)

class Punch(Attack):
    def __init__(self):
        super(Punch, self).__init__('punch', 5, 10, 90)

class Kick(Attack):
    def __init__(self):
        super(Kick, self).__init__('kick', 15, 20, 75)

class HammerSmash(Attack):
    def __init__(self):
        super(HammerSmash, self).__init__('hammer smash', 50, 60, 17)
