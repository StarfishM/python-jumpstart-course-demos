import journal

def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------')
    print('      Journal APP')
    print('-------------------------')
    print()


def run_event_loop():
    print('Hey your journal app is running, what do you want to do?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal.load(journal_name)  # list()

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(
                "I only understand these three commands A, L and x dum dum, I don't know what to do with '{}'.".format(
                    cmd))

    print('Done, Yay')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Hey these are your journal entries: ")
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))


def add_entry(data):
    text = input("type your entry <enter> to leave this place: ")
    journal.add_entry(text, data)
    # data.append(text)


if __name__ == '__main__':
    main()
