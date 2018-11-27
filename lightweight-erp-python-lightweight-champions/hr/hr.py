""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    ui.print_menu(
        "Accounting",
        [
            "(1) Show table",
            "(2) Add",
            "(3) Remove",
            "(4) Update",
            "(5) Who is the oldest person?",
            "(6) Who is the closest to the average age?"
        ],
        "(0) Back to main menu"
    )
    while True:
        inputs = input("Choose an option: ")
        option = inputs[0]
        if option == "1":
            show_table(hr_table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            which_year_max(table)
        elif option == "6":
            avg_amount(table, year)
        elif option == "0":
            return
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    hr_title = ["ID", "Name", "Birth year"]
    hr_table = data_manager.get_table_from_file("../hr/persons.csv")  # stuck here
    ui.print_table(hr_table, hr_title)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (li   st): table to add new record to

    Returns:
        list: Table with a new record
    """

    user_inputs = ["Name: ", "Birth year: "]

    # to common.py?
    while True:
        try:
            given_inputs = ui.get_inputs(user_inputs, "Please provide added information")
            given_inputs[1] = int(given_inputs[1])  # birth year validation
            if given_inputs[1] in range(1900, 2020):
                break
            else:
                print("Type in a valid year!\n")
        except ValueError:
            print("Type in a year with numbers!\n")

    random_ID = common.generate_random(table)

    table[0].append(random_ID)
    for i in range(len(user_inputs)):
        table[i+1].append(user_inputs[i])

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code


def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    # your code
