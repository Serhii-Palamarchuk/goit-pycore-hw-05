# Завдання 4
# Доробіть консольного бота помічника з попереднього домашнього завдання та додайте обробку помилок за допомоги декораторів.

def input_error(func):
    """
    A decorator function that handles common input errors.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    function: The decorated function.

    Raises:
    KeyError: If a key error occurs.
    ValueError: If a value error occurs.
    IndexError: If an index error occurs.
    Exception: If any other exception occurs.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return str(e)
        except ValueError as e:
            return str(e)
        except IndexError as e:
            return str(e)
        except Exception as e:
            return "An error occurred. Please try again."
    return inner

@input_error
def parse_input(user_input):
    """
    Parses the user input and returns the command and arguments.

    Args:
        user_input (str): The user input to be parsed.

    Returns:
        tuple: A tuple containing the command (str) and arguments (list).

    Example:
        >>> parse_input("add 1 2 3")
        ('add', ['1', '2', '3'])
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Args:
        args (list): A list of two elements - name and phone.
        contacts (dict): A dictionary containing existing contacts.

    Returns:
        str: A message indicating the result of the operation.
    """
    if len(args) != 2:
        raise ValueError("Invalid arguments. Usage: add [name] [phone]")
    name, phone = args
    if name in contacts:
        raise KeyError("Contact already exists.")
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Change the phone number of a contact.

    Args:
        args (list): A list of two elements - [name, new phone].
        contacts (dict): A dictionary containing contact names as keys and phone numbers as values.

    Returns:
        str: A message indicating whether the contact was successfully updated or not.
    """
    if len(args) != 2:
        raise ValueError("Invalid arguments. Usage: change [name] [new phone]")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError("Contact not found.")

@input_error
def show_phone(args, contacts):
    """
    Display the phone number of a contact.

    Args:
        args (list): A list of arguments. Should contain only one element, which is the name of the contact.
        contacts (dict): A dictionary containing contact names as keys and phone numbers as values.

    Returns:
        str: The phone number of the contact if found, or an error message if the contact is not found.
    """
    if len(args) != 1:
        raise ValueError("Invalid arguments. Usage: phone [name]")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found.")

@input_error
def show_all(contacts):
    """
    Returns a formatted string representation of all contacts.

    Args:
        contacts (dict): A dictionary containing contact names as keys and phone numbers as values.

    Returns:
        str: A formatted string representation of all contacts, with each contact's name and phone number separated by a colon.

    Example:
        >>> contacts = {'John': '1234567890', 'Jane': '9876543210'}
        >>> show_all(contacts)
        'John: 1234567890\nJane: 9876543210'
    """
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def main():
    """
    The main function of the assistant bot program.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()