# Your code here
import random
from utils.table import Seat, Table
class Openspace:
    """It represente the room/open space and is able to deal with table and a set number of table as a integer."""
    def __init__(self, tables: list = None, number_of_tables: int = 6, table_capacity: int = 4):
        self.number_of_tables = number_of_tables
        self.tables= tables if tables is not None else [Table(capacity=table_capacity) for _ in range(number_of_tables)]

    def organize(self, names):
        random.shuffle(names)#simply randomise and shuffle the list of names it's all we need for randoms assignement.
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
        for people, table in enumerate(self.tables):
            print(f"Table {people + 1}:")
            for seat in table.seats:
                print(f"  - {seat}")
    def store(self, filename):
        with open(filename, 'w') as f:
            for people, table in enumerate(self.tables):
                f.write(f"Table {people + 1}:\n")
                for seat in table.seats:
                    f.write(f"  - {seat}\n")
    def __str__(self):
        return f"Openspace with {self.number_of_tables} tables and the following seating arrangements: {[str(table) for table in self.tables]}"