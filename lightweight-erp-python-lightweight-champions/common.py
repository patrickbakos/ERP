""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = ''

    # must implement check if ID is unique
    for line in table:
        if line[0] == generated or generated == "":
            generated = ''.join(random.choice("!#$%&'*+,-.:<=>?@^_`|~") + random.choice("0123456789")
                                + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                                + random.choice("abcdefghijklmnopqrstuvwxyz") for e in range(2))

    return generated
