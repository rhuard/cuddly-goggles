from dude import PlayerDude, CPUDude
from attack import *

if __name__ == '__main__':
    # give each their own attack
    # the [] makes this a list of attack objects
    dude1 = PlayerDude([Fireball(), Kick()])
    dude2 = CPUDude([Punch(), HammerSmash()])

    while True:
        print('dude1(health {}) attack'.format(dude1.health))
        dude1.attack(dude2)
        if dude2.health < 0:
            print('Dude1 wins')
            exit(0)
        input('##################\npress any key to continue....')
        print('##################\ndude2(health {}) attack'.format(dude2.health))
        dude2.attack(dude1)
        if dude1.health < 0:
            print('Dude2 wins')
            exit(0)
        print('##################')


