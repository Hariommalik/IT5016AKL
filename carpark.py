class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_lot = {}

    def park_car(self, license_plate):
        if len(self.parking_lot) < self.capacity:
            if license_plate not in self.parking_lot:
                self.parking_lot[license_plate] = True
                print(f"Car with license plate {license_plate} parked.")
            else:
                print(f"Car with license plate {license_plate} is already parked.")
        else:
            print("Parking lot is full!")

    def remove_car(self, license_plate):
        if license_plate in self.parking_lot:
            del self.parking_lot[license_plate]
            print(f"Car with license plate {license_plate} removed.")
        else:
            print(f"No car with license plate {license_plate} found.")

    def display_parking_lot(self):
        if not self.parking_lot:
            print("Parking lot is empty.")
        else:
            print("Currently parked cars:")
            for license_plate in self.parking_lot:
                print(f"- {license_plate}")

def main():
    capacity = int(input("Enter parking lot capacity: "))
    parking_lot = ParkingLot(capacity)

    while True:
        print("\nOptions:")
        print("1. Park Car")
        print("2. Remove Car")
        print("3. Display Parking Lot")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            license_plate = input("Enter car license plate: ")
            parking_lot.park_car(license_plate)
        elif choice == '2':
            license_plate = input("Enter car license plate: ")
            parking_lot.remove_car(license_plate)
        elif choice == '3':
            parking_lot.display_parking_lot()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
