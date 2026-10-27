from abc import ABC, abstractmethod


# ==========================================
# CLASS 1: FLIGHT
# Stores flight details and manages seats
# ==========================================

class Flight:

    def __init__(
        self,
        flight_code,
        airline,
        source,
        destination,
        available_seats,
        base_fare
    ):
        self.__flight_code = flight_code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__available_seats = available_seats
        self.__base_fare = base_fare

    @property
    def flight_code(self):
        return self.__flight_code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def available_seats(self):
        return self.__available_seats

    @property
    def base_fare(self):
        return self.__base_fare

    def display_flight(self):
        print(
            f"{self.__flight_code:<10}"
            f"{self.__airline:<15}"
            f"{self.__source:<15}"
            f"{self.__destination:<15}"
            f"{self.__available_seats:<10}"
            f"Rs. {self.__base_fare}"
        )

    def has_enough_seats(self, ticket_count):
        return ticket_count <= self.__available_seats

    def reserve_seats(self, ticket_count):
        if self.has_enough_seats(ticket_count):
            self.__available_seats -= ticket_count
            return True

        return False


# ==========================================
# CLASS 2: PASSENGER (ABSTRACT BASE CLASS)
# ==========================================

class Passenger(ABC):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def get_discount_rate(self):
        pass

    @abstractmethod
    def get_passenger_type(self):
        pass


# ==========================================
# CLASS 3: REGULAR PASSENGER
# Discount = 0%
# ==========================================

class RegularPassenger(Passenger):

    def get_discount_rate(self):
        return 0

    def get_passenger_type(self):
        return "Regular"


# ==========================================
# CLASS 4: STUDENT PASSENGER
# Discount = 10%
# ==========================================

class StudentPassenger(Passenger):

    def get_discount_rate(self):
        return 10

    def get_passenger_type(self):
        return "Student"


# ==========================================
# CLASS 5: BOOKING
# Stores confirmed booking information
# ==========================================

class Booking:

    def __init__(
        self,
        booking_id,
        passenger,
        flight,
        ticket_count
    ):
        self.__booking_id = booking_id
        self.__passenger = passenger
        self.__flight = flight
        self.__ticket_count = ticket_count

        self.__subtotal = (
            flight.base_fare * ticket_count
        )

        self.__discount = (
            self.__subtotal
            * passenger.get_discount_rate()
            / 100
        )

        self.__final_amount = (
            self.__subtotal - self.__discount
        )

    def display_summary(self):

        print("\n" + "=" * 45)
        print("           BOOKING CONFIRMED")
        print("=" * 45)

        print(f"Booking ID       : {self.__booking_id}")
        print(f"Passenger Name   : {self.__passenger.name}")
        print(f"Passenger Age    : {self.__passenger.age}")
        print(
            f"Passenger Type   : "
            f"{self.__passenger.get_passenger_type()}"
        )

        print(f"Flight Code      : {self.__flight.flight_code}")
        print(f"Airline          : {self.__flight.airline}")
        print(
            f"Route            : "
            f"{self.__flight.source} to "
            f"{self.__flight.destination}"
        )

        print(f"Number of Tickets: {self.__ticket_count}")

        print(
            f"Base Fare        : "
            f"Rs. {self.__flight.base_fare:.2f}"
        )

        print(f"Subtotal         : Rs. {self.__subtotal:.2f}")

        print(
            f"Discount "
            f"({self.__passenger.get_discount_rate()}%): "
            f"Rs. {self.__discount:.2f}"
        )

        print(f"Final Amount     : Rs. {self.__final_amount:.2f}")

        print("=" * 45)


# ==========================================
# CLASS 6: FLIGHT BOOKING SYSTEM
# Controls the complete application
# ==========================================

class FlightBookingSystem:

    def __init__(self):

        self.__flights = [
            Flight(
                "PN101",
                "IndiGo",
                "Pune",
                "Delhi",
                20,
                4000
            ),

            Flight(
                "MB202",
                "Air India",
                "Mumbai",
                "Bengaluru",
                15,
                5000
            ),

            Flight(
                "PH303",
                "SpiceJet",
                "Pune",
                "Hyderabad",
                18,
                3500
            )
        ]

        self.__bookings = []
        self.__next_booking_number = 1001

    # --------------------------------------
    # Display all available flights
    # --------------------------------------

    def display_flights(self):

        print("\n" + "=" * 80)
        print("                  AVAILABLE FLIGHTS")
        print("=" * 80)

        print(
            f"{'Code':<10}"
            f"{'Airline':<15}"
            f"{'Source':<15}"
            f"{'Destination':<15}"
            f"{'Seats':<10}"
            f"Base Fare"
        )

        print("-" * 80)

        for flight in self.__flights:
            flight.display_flight()

        print("=" * 80)

    # --------------------------------------
    # Find a flight using its code
    # --------------------------------------

    def find_flight_by_code(self, flight_code):

        for flight in self.__flights:

            if flight.flight_code == flight_code.upper():
                return flight

        return None

    # --------------------------------------
    # Validate booking details
    # --------------------------------------

    def validate_booking_details(
        self,
        flight,
        name,
        age,
        ticket_count
    ):

        if flight is None:
            print("Error: Invalid flight code.")
            return False

        if not name.strip():
            print("Error: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return False

        if ticket_count <= 0:
            print("Error: Ticket count must be greater than zero.")
            return False

        if not flight.has_enough_seats(ticket_count):
            print("Booking failed: Not enough seats available.")
            return False

        return True

    # --------------------------------------
    # Create passenger object
    # --------------------------------------

    def create_passenger(self, name, age, passenger_type):

        passenger_type = passenger_type.strip().lower()

        if passenger_type == "student":
            return StudentPassenger(name, age)

        if passenger_type == "regular":
            return RegularPassenger(name, age)

        return None

    # --------------------------------------
    # Book a flight
    # --------------------------------------

    def book_flight(self):

        print("\n========== BOOK A FLIGHT ==========")

        self.display_flights()

        flight_code = input(
            "Enter flight code: "
        ).strip().upper()

        flight = self.find_flight_by_code(flight_code)

        name = input(
            "Enter passenger name: "
        ).strip()

        try:
            age = int(input("Enter passenger age: "))
        except ValueError:
            print("Error: Age must be a valid whole number.")
            return

        passenger_type = input(
            "Passenger type (Regular/Student): "
        ).strip()

        passenger = self.create_passenger(
            name,
            age,
            passenger_type
        )

        if passenger is None:
            print(
                "Error: Passenger type must be "
                "Regular or Student."
            )
            return

        try:
            ticket_count = int(
                input("Enter number of tickets: ")
            )
        except ValueError:
            print("Error: Ticket count must be a whole number.")
            return

        # Validate everything before changing seat counts.

        if not self.validate_booking_details(
            flight,
            name,
            age,
            ticket_count
        ):
            print("No booking was created.")
            return

        # Reserve seats only after all validations succeed.

        if not flight.reserve_seats(ticket_count):
            print("Booking failed: Not enough seats available.")
            print("No booking was created.")
            return

        # Create and store the confirmed booking.

        booking_id = f"BK{self.__next_booking_number}"

        booking = Booking(
            booking_id,
            passenger,
            flight,
            ticket_count
        )

        self.__bookings.append(booking)
        self.__next_booking_number += 1

        booking.display_summary()

    # --------------------------------------
    # Display the latest confirmed booking
    # --------------------------------------

    def view_booking(self):

        if not self.__bookings:
            print("\nNo confirmed booking exists yet.")
            return

        print("\nDisplaying the most recent booking:")

        self.__bookings[-1].display_summary()

    # --------------------------------------
    # Main menu
    # --------------------------------------

    def run(self):

        print("\nWelcome to Kiran Air Booking!")

        while True:

            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":

                self.display_flights()

            elif choice == "2":

                self.book_flight()

            elif choice == "3":

                self.view_booking()

            elif choice == "4":

                print(
                    "\nThank you for using "
                    "Kiran Air Booking!"
                )
                break

            else:

                print(
                    "Invalid choice. "
                    "Please enter a number from 1 to 4."
                )


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    application = FlightBookingSystem()

    application.run()