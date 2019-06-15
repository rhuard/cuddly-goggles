class Dude():
    def __init__(self):
        self.health = 100

    def attack(self, target):
        damage = 40
        target.health -= damage

    def getHealth(self):
        return self.health


if __name__ == '__main__':
    dude1 = Dude()
    dude2 = Dude()

    while True:
        dude1.attack(dude2)
        if dude2.getHealth() < 0:
            print 'Dude1 wins'
            exit(0)
        dude2.attack(dude1)
        if dude1.getHealth() < 0:
            print 'Dude2 wins'
            exit(0)

