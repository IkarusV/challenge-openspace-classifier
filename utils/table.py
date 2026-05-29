class Seat:
    """class representing a seat in the openspac, able to take a bolean value and an occupant.
    param free: a boolean value representing if the seat is free or not, default is True.
    param occupant: a string representing the name of the occupant of the seat, default is None.
    return: The specified free status and occupant, and the ability to set and remove occupants and represent itself as a string."""
    def __init__(self, free: bool = True, occupant: str = None):
        self.free = free
        self.occupant = occupant
    def set_occupant(self, occupant: str)->:
        """Set the occupant of the seat and mark it as occupied.
        :param occupant: A string representing the name of the occupant to be assigned to the seat.
        :return: None. The function will modify the state of the Seat instance by setting the occupant and marking the seat as occupied."""
        self.occupant = occupant
        self.free = False
    def remove_occupant(self) -> str:
        """Remove the occupant from the seat and mark it as free.
        :param None.
        :return: A string representing the name of the occupant who was removed."""
        removed = self.occupant # to store the occupant name before we remove him, a temporary variable.
        self.free = True 
        self.occupant = None
        return removed # we return the temporary variable who know the previous occupent name.
    def __str__(self):
        """Return a string representation of the seat, indicating whether it is free or occupied and by whom.
        :param None.
        :return: A string representing the seat. If the seat is free, it will indicate that it is free; if occupied, it will indicate the name of the occupant."""
        return f"Seat: {'Free' if self.free else f'Occupied by {self.occupant}'}"




class Table:
    """class representing a table in the openspace,it take a capacity as a int ( number of seats).
    param capacity: an integer representing the number of seats at the table, default is 4.
    return: a table class with the specified capacity, a list of Seat instances representing the seats at the table, and methods to check for free spots, assign occupants to seats, calculate remaining capacity, and represent itself as a string."""
    def __init__(self, capacity: int = 4):
        self.capacity = int(capacity)
        self.seats = [Seat() for _ in range(self.capacity)] # since we don't take the seats as an argument, here we create seats based on the capacity inputed.
    def has_free_spot(self)-> bool:
        """Check if there is at least one free spot at the table.
        :param None.
        :return: A boolean value indicating whether there is at least one free spot."""
        for seat in self.seats:
            if seat.free:
                return True
        return False
    def assign_seat(self, name="New Occupant") -> None:
        """take an occupant and assign it to a seat
        :param name: take a string name that will be the new occupant of the seat
        :return: nothing, but print "no free spot avaliables" if  no free spot is found and also modify the Seat object"""
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    break
        else:
            print("No free spots available at the table.")
    def left_capacity(self) -> int:#should return an integer representing the number of free seats left at the table
        """Calculate the number of free seats left at the table.
        :param None.
        :return: An integer representing the number of free seats left at the table."""
        occupied_seats = sum(not seat.free for seat in self.seats)
        return self.capacity - occupied_seats
    def __str__(self):
        """Return a string representation of the table, including its capacity and the status of each seat.
        :param None.
        :return: A string representing the table."""
        return f"Table with {self.capacity} seats: {', '.join(str(seat) for seat in self.seats)}"