from actors import Wizard,Creature

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
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Creature('Bat', 3),
        Creature('Dragon', 50),
        Creature('Evil Wizard', 1000)

    ]

    hero = Wizard('Gandolf', 75)

    while True:

        cmd = input('Do you [s]mile, [r]un away or [l]ook around?')
        if cmd == 's':
            print('smile')
        elif cmd == 'r':
            print('run away')
        elif cmd == 'l':
            print('look around')
        else:
            print("Sorry but you did not understand my complex rules, that command does not exist... exiting game now, bye!")
            break


if __name__ == '__main__':
    main()
