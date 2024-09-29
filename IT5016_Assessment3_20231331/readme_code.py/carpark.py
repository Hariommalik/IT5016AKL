class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_slots = {}
        self.current_count = 0

    def park_car(self, car_number):
        if self.current_count < self.capacity:
            if car_number in self.parking_slots:
                print(f"Car {car_number} is already parked.")
            else:
                self.parking_slots[car_number] = True
                self.current_count += 1
                print(f"Car {car_number} parked successfully.")
        else:
            print("Parking lot is full!")

    def unpark_car(self, car_number):
        if car_number in self.parking_slots:
            del self.parking_slots[car_number]
            self.current_count -= 1
            print(f"Car {car_number} unparked successfully.")
        else:
            print(f"Car {car_number} not found in the parking lot.")

    def available_slots(self):
        return self.capacity - self.current_count

    def parked_cars(self):
        return list(self.parking_slots.keys())

def main():
    parking_lot = ParkingLot(capacity=5)

    while True:
        print("\n1. Park Car")
        print("2. Unpark Car")
        print("3. Check Available Slots")
        print("4. List Parked Cars")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            car_number = input("Enter car number to park: ")
            parking_lot.park_car(car_number)
        elif choice == '2':
            car_number = input("Enter car number to unpark: ")
            parking_lot.unpark_car(car_number)
        elif choice == '3':
            print(f"Available slots: {parking_lot.available_slots()}")
        elif choice == '4':
            parked = parking_lot.parked_cars()
            if parked:
                print("Parked cars:", ", ".join(parked))
            else:
                print("No cars parked.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
