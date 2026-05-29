from utils.table import Seat, Table
from utils.openspace import Openspace
from utils.file_utils import get_names_by_lines

Collegues = "new_colleagues.csv" #input file to modify for another execels name files.
final_output_name = "output.csv" #the name of final output.

def main():
    """Run the openspace organizer(take a list of names from a file to then shuffle,organise them and display it before saving it into a files)."""
    
    names = get_names_by_lines(Collegues)

    openspace = Openspace(number_of_tables=6, table_capacity=4)

    openspace.organize(names)

    openspace.display()

    openspace.store(final_output_name)
    print(f"Results saved to {final_output_name}")

main()