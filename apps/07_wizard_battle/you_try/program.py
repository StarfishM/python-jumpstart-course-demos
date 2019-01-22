from actors import Creature, Wizard, Dragon, SmallAnimal
import random
import time


def main():
    print_the_header()
    game_loop()


def print_the_header():
    print('---------------------------------------------------------------')
    print("  * Welcome to this utterly complex and amazing game I made *")
    print('---------------------------------------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 75)

    ]
    #print(creatures)

    hero = Wizard('Gandolf', 75)


    while True:
        active_creature = random.choice(creatures)
        print("A {} of level {} has appeared from the dark and misty forest grounds..."
               .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [s]mile, [r]un away or [l]ook around?')
        if cmd == 's':
            if hero.smile(active_creature):
                creatures.remove(active_creature)
            else:
                print("Your wizard has been defeated and needs to regain strength")
                time.sleep(5)
                print("The wizard returns to pick up another battle of smiles")
                print()

        elif cmd == 'r':
            print('The wizard unsure of his strength runs and hides')
            print()
        elif cmd == 'l':
            print('The wizard {} takes a look around the forest and sees:'.format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
            print()

        else:
            print("Sorry but you did not understand my complex rules, that command does not exist... exiting game now, bye!")
            break

        if not creatures:
            print("Congratulations, you have defeated all creatures you have saved the holy grapes")
            print("----  / ----")
            print("--- ()() ---")
            print("-- ()()() --")
            print("--- ()() ---")
            print("---- () ----")
            break



if __name__ == '__main__':
    main()
