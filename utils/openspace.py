# Your code here
import random
from utils.table import Seat, Table
class Openspace:
    """Function that will represent the open space and manage each tables.

    :param tables: the list of tables, if not provided it will create a default list of tables based on the number of tables and their capacity.
    :param number_of_tables:the number of tables in the open space, default is 6.
    :param table_capacity: the capacity of each table, default is 4.
    :return: an instance of the Openspace class with the specified number of tables and their capacity and the ability to organize, display and store the arrangements and seating."""
    def __init__(self, tables: list = None, number_of_tables: int = 6, table_capacity: int = 4):
        self.number_of_tables = number_of_tables
        self.tables= tables if tables is not None else [Table(capacity=table_capacity) for _ in range(number_of_tables)]#I use none so it's safer as a default argument rather than empty, easier to work with and avoid mutable argument.

    def organize(self, names: list):
        """Shuffles the names before organizing them into different tables.
        :param names: a list of strings representing the names to be organized.
        :return: None, but the function will modify the state of the Openspace instance by assigning names to tables based on the shuffled order."""
        random.shuffle(names)  # simply randomize and shuffle the list of names it's all we need for random assignment.
        for name in names:
            assigned = False
            for table in self.tables:#we loop throught the tables to check any free space then we find one, we break, then do it all again.
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned = True
                    break
            if not assigned:
                print(f"No free spots available for {name}.")
    def display(self):
        """Display the final result of the open space layout.
        :param None.
        :return: None, but the function will print the seating for each table to the console."""
        for i, table in enumerate(self.tables):#using the intex t oget the number of the table, plus 1 to count in a human fashion.
            print(f"Table {i + 1}:")
            for seat in table.seats:
                print(f"  - {seat}")
    def store(self, filename: str):
        """Store the final result of the openspace layout in a file.
        :param filename: A string representing the path to the file where the results will be saved.
        :return: None, but the function will write the arrangements and seating to the specified file."""
        with open(filename, 'w') as f:
            for i, table in enumerate(self.tables):#it open a files to writte,emunerate allow us to take the number of the table plus the table itself, then we don't need number for the seats a for classic for loop is enouph.
                f.write(f"Table {i + 1}:\n")
                for seat in table.seats:#\n is to also have a new lines since it won't otherwise
                    f.write(f"  - {seat}\n")
    def __str__(self):
        """Return a string representation of the openspace instance.
        :param None.
        :return: A string representing the openspace."""
        return f"Openspace with {self.number_of_tables} tables and the following seating arrangements: {[str(table) for table in self.tables]}"