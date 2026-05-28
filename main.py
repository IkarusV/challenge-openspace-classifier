from utils.table import Seat, Table
from utils.openspace import Openspace
from utils.file_utils import get_names_by_lines


def main():
    """Run the openspace organizer."""
    
    names = get_names_by_lines("new_colleagues.csv")

    openspace = Openspace(number_of_tables=6, table_capacity=4)

    openspace.organize(names)

    openspace.display()

    openspace.store("output.csv")
    print("Results saved to output.csv")


if __name__ == "__main__":
    main()