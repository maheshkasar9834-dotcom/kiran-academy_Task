import random

print("===================================")
print("       CAB BOOKING CHATBOT")
print("===================================")

while True:

    # Main Menu
    print("\n========== MAIN MENU ==========")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ").strip()

    # Exit
    if choice == "2":
        print("\nThank you for using Cab Booking Chatbot!")
        print("Goodbye!")
        break

    # Invalid Main Menu Choice
    elif choice != "1":
        print("\nInvalid choice! Please select 1 or 2.")
        continue

    # Select Cab Type
    print("\n========== SELECT CAB TYPE ==========")
    print("1. Auto  - Rs. 12/km")
    print("2. Sedan - Rs. 18/km")
    print("3. SUV   - Rs. 25/km")

    cab_choice = input("Select your cab: ").strip()

    if cab_choice == "1":
        cab_type = "Auto"
        rate = 12

    elif cab_choice == "2":
        cab_type = "Sedan"
        rate = 18

    elif cab_choice == "3":
        cab_type = "SUV"
        rate = 25

    else:
        print("\nInvalid cab choice!")
        print("Returning to the main menu...")
        continue

    # Select Route
    print("\n========== SELECT ROUTE ==========")
    print("1. Pune Station to Shivajinagar - 5 km")
    print("2. Swargate to Kothrud - 8 km")
    print("3. Hinjawadi to Wakad - 10 km")

    route_choice = input("Select your route: ").strip()

    if route_choice == "1":
        source = "Pune Station"
        destination = "Shivajinagar"
        distance = 5

    elif route_choice == "2":
        source = "Swargate"
        destination = "Kothrud"
        distance = 8

    elif route_choice == "3":
        source = "Hinjawadi"
        destination = "Wakad"
        distance = 10

    else:
        print("\nInvalid route choice!")
        print("Returning to the main menu...")
        continue

    # Calculate Fare
    fare = distance * rate

    # Display Booking Details
    print("\n========== RIDE DETAILS ==========")
    print("Cab Type      :", cab_type)
    print("Source        :", source)
    print("Destination   :", destination)
    print("Distance      :", distance, "km")
    print("Rate per km   : Rs.", rate)
    print("Total Fare    : Rs.", fare)

    # Booking Confirmation
    print("\n========== BOOKING CONFIRMATION ==========")
    print("1. Confirm & Share OTP")
    print("2. Cancel Ride")

    confirm_choice = input("Enter your choice: ").strip()

    if confirm_choice == "1":

        # Generate 4-digit OTP
        otp = random.randint(1000, 9999)

        print("\nYour OTP is:", otp)
        print("Booking Confirmed Successfully!")

        print("\nIMPORTANT:")
        print("Ride cancellation is not allowed after OTP sharing.")

    elif confirm_choice == "2":

        print("\nRide cancelled successfully!")
        print("No OTP has been shared.")

    else:

        print("\nInvalid confirmation choice!")
        print("Booking was not confirmed. No OTP has been shared.")

    # Return to Main Menu
    print("\nReturning to the main menu...")