class Flight():
    def __init__(self,seats):
        self.seats = seats
        self.passengers  = []
    
    def booking(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True
    
    def openSeats(self):
        return self.seats  - len(self.passengers)

mai = Flight(3)

for person in ["Harry","Draco","Ron","Luna"]: 
    if mai.booking(person): 
        print(f"{person}'s booking completed successfully!")
    else:
        print(f"No available seats for {person}")