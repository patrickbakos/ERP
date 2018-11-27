import ui
import data_manager
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
    table = data_manager.get_table_from_file(file_name = "accounting/items.csv")

    print("Which label do you want to update?")
    print("month\nday\nyear\type\namount")
    user_choice = input()
    for line in table:
        if id_ in line:
            if user_choice == "month":
                line[1] = input()
            elif user_choice == "day":
                line[2] = input()
            elif user_choice == "year":
                line[3] = input()
            elif user_choice == "type":
                line[4] = input()
            elif user_choice == "amount":
                line[5] = input()
        else:
            continue
        break

    return table
update(table = "accounting/items.csv", id_ = "kH14Ju#&")