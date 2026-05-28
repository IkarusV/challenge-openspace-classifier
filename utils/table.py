class Seat:
    """class representing a seat in the openspac, able to take a bolean value and an occupant."""
    def __init__(self, free: bool = True, occupant: str = None):
        self.free = free
        self.occupant = occupant
    def set_occupant(self, occupant):
        self.occupant = occupant
        self.free = False
    def remove_occupant(self):
        removed = self.occupant # to store the occupant name before we remove him, a temporary variable.
        self.free = True 
        self.occupant = None
        return removed # we return the temporary variable who know the previous occupent name.
    def __str__(self):
        return f"Seat: {'Free' if self.free else f'Occupied by {self.occupant}'}"




class Table:
    """class representing a table in the openspace,it take a capacity as a int ( number of seats)."""
    def __init__(self, capacity: int = 4):
        self.capacity = int(capacity)
        self.seats = [Seat() for _ in range(self.capacity)] # since we don't take the seats as an argument, here we create seats based on the capacity inputed.
    def has_free_spot(self):
        for seat in self.seats:
            if seat.free:
                return True
        return False
    def assign_seat(self, name="New Occupant"):
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    break
        else:
            print("No free spots available at the table.")
    def left_capacity(self):#should return an integer representing the number of free seats left at the table
        occupied_seats = sum(not seat.free for seat in self.seats)
        return self.capacity - occupied_seats
    def __str__(self):
        return ", ".join(str(seat) for seat in self.seats)