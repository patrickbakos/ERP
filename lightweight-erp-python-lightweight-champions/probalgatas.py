import ui
import data_manager

def sortalpha(table, label_index):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indexed_alphabet = enumerate(alphabet_lower)
    current = 0
    sorted_list = []
    for letter in alphabet_lower:
        for line in table:
            if line[1][1] == " ":
                sorted_list.append(line)
            else:
                if line[1][1] == letter:
                    sorted_list.append(line)

    return sorted_list

table = data_manager.get_table_from_file("sales/sales.csv")
sortedjana = sortalpha(table, 1)
ui.print_table(sortedjana, ["ID", "Title", "Copies", "Month", "Day", "Year"])
