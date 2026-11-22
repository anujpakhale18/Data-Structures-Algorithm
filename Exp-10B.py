class ParkingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, vehicle_number):
        return vehicle_number % self.size

    def insert(self, vehicle_number):
        index = self.hash_function(vehicle_number)

        for step in range(self.size):
            pos = (index + step) % self.size

            if self.table[pos] == vehicle_number:
                print("Vehicle already allocated:", vehicle_number)
                return False

            if self.table[pos] is None:
                self.table[pos] = vehicle_number
                return True

        print("All parking slots are full. Cannot allocate", vehicle_number)
        return False

    def search(self, vehicle_number):
        home = self.hash_function(vehicle_number)

        for step in range(self.size):
            pos = (home + step) % self.size

            if self.table[pos] is None:
                return -1

            if self.table[pos] == vehicle_number:
                return pos

        return -1

    def display(self):
        print("\nParking Slot Allocation:")
        print("Slot\tVehicle Number")
        print("----------------------")

        for index, vehicle in enumerate(self.table):
            print(index, "\t", vehicle if vehicle is not None else "EMPTY")


def main():
    size = int(input("Enter number of parking slots: "))

    if size <= 0:
        print("Number of parking slots must be greater than zero.")
        return

    parking = ParkingHashTable(size)

    n = int(input("Enter number of vehicles: "))

    if n < 0:
        print("Number of vehicles cannot be negative.")
        return

    for i in range(n):
        vehicle_number = int(
            input(f"Enter vehicle number {i + 1}: ")
        )
        parking.insert(vehicle_number)

    parking.display()

    search_vehicle = int(
        input("\nEnter vehicle number to find parking slot: ")
    )

    position = parking.search(search_vehicle)

    if position != -1:
        print("Vehicle found at parking slot", position)
    else:
        print("Vehicle not found")


if __name__ == "__main__":
    main()