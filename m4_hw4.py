def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contacts(args, contacts):
    if len(args) != 2:
        print("Input error, please usage: add [name] [phone number]")
        return
    name, phone = args
    contacts[name] = phone
    return "contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        print("Input error, please usage: add [name] [phone number]")
        return
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact is not found"


def phone_username(args, contacts):
    if len(args) != 1:
        print("Input error, please usage: add [name] [phone number]")
        return
    name = args[0]
    if name in contacts:
        return f"Contact {name} : {contacts[name]}"
    else:
        return "Contact is not found"


def show_all_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"contact {name} : {phone}")
    else:
        return "Phonebook is empty"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contacts(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(phone_username(args, contacts))
            case "all":
                show_all_contacts(contacts)
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
