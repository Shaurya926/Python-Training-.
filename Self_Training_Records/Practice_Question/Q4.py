# Write a program using switch case to display the name of the month based on the month number entered by the user.
def month_name(month_number):
    switcher = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switcher.get(month_number, "Invalid month number")
# Get user input
try:
    month_number = int(input("Enter the month number (1-12): "))
    print("The month is:", month_name(month_number))
except ValueError:
    print("Please enter a valid integer.")
    