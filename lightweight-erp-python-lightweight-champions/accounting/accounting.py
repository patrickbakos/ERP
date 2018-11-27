""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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
            "(5) Which year max?",
            "(6) AVG amount"
        ],
        "(0) Back to main menu"
    )
    while True:
        inputs = input("Choose an option: ")
        option = inputs[0]
        if option == "1":
            show_table(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "2":
            add(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "3":
            id_ = inputs("ID? ")[0]
            remove(data_manager.get_table_from_file("accounting/items.csv"), id_)
        elif option == "4":
            id_ = inputs("ID? ")[0]
            update(data_manager.get_table_from_file("accounting/items.csv"), id_)
        elif option == "5":
            which_year_max(data_manager.get_table_from_file("accounting/items.csv"))
        elif option == "6":
            year = inputs("Year? ")[0]
            avg_amount(data_manager.get_table_from_file("accounting/items.csv"), year)
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

    # your code
    titles = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    table = data_manager.get_table_from_file("accounting/items.csv")
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    
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
    table = data_manager.get_table_from_file(file_name="accounting/items.csv")
    for line in table:
        if id_ in line:
            table.remove(line)

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
    table = data_manager.get_table_from_file(file_name="accounting/items.csv")
    ui.get_inputs(mivan)
    

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
