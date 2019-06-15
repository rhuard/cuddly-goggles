from dude import Dude
from attack import *

if __name__ == '__main__':
    # give each their own attack
    dude1 = Dude(Fireball())
    dude2 = Dude(Punch())

    while True:
        print('dude1(health {}) attack'.format(dude1.health)) # just making it easier to track who has what health
        dude1.attack(dude2)
        if dude2.health < 0:
            print('Dude1 wins')
            exit(0)
        input('\n##################\npress any button to proceed to next round...') # simple way to slow down simulation so it easier to follow
        print('##################\ndude2(health {}) attack'.format(dude2.health))
        dude2.attack(dude1)
        if dude1.health < 0:
            print('Dude2 wins')
            exit(0)
        input('\n##################\npress any button to proceed to next round...')
        print('##################')


