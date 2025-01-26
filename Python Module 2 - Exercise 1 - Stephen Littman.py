'''
Exercise 1
Using your course text, Title: Programming Logic & Design Edition: 10th.

Complete Chapter 2, Programming Exercise #7 on page 61. Design the logic for Hazel's Housecleaning Service program using the flowchart. 
Please review all necessary steps and carefully consider the materials and structure needed to make a flowchart in Raptor and a Python program.
Use the information you learned about grouping code sections and plan your processes.
Outline the logic for a program that calculates Hazel's Housecleaning service charges.
The planning section - lets us get started

Declare any required variables.
Based on the rest of the information, what variables are needed?
Collecting the input

Ask the user to input a customer's last name.
The user will input the number of bathrooms to be cleaned
The user will input the number of other rooms to be cleaned.
The service charge will be $40 plus $15 for each bathroom and $10 for each other room.
Print - the information collected with the service charge and total amount.

Display the customer's name
Display the number of bathrooms and the cost to clean
Display the number of other rooms and the total cost of the other rooms to clean
Display the total cost of the bathrooms and other rooms.
Display a message indicating the program is complete.
'''

#initialization
BASE_COST = 40.00
BATHROOM_COST = 15.00
ROOM_COST = 10.00
totalBathroomCost = 0.00
totalRoomCost = 0.00
totalCost = 0.00
lastName = ""
bathrooms = 0
rooms = 0


# houseKeeping function gets last name
def houseKeeping():
    global lastName
    lastName = input("Please enter your last name: ")
    return


# functionality loop
def detailLoop():
    global lastName
    while lastName != "ZZZZ":
        bathrooms = int(input("Please enter the amount of bathrooms that need to be cleaned: "))
        rooms = int(input("Please enter the amount of rooms that need to be cleaned: "))
        totalBathroomCost = bathrooms * BATHROOM_COST
        totalRoomCost = rooms * ROOM_COST
        totalCost = totalBathroomCost + totalRoomCost + BASE_COST
        print(f"Customer's Last Name: " + lastName)
        print(f"Number of bathrooms to be cleaned: {bathrooms}")
        print(f"Cost to clean bathrooms: ${totalBathroomCost:.2f}.")
        print(f"Number of other rooms to be cleaned: {rooms}")
        print(f"Total cost for cleaning other rooms: ${totalRoomCost:.2f}.")
        print(f"Total cost for bathrooms and other rooms: ${totalCost:.2f}.")
        lastName = input("Please enter your last name: ")
    return


# end of program
def endOfJob():
    print("The program has ended.")
    return


# main function
def main():
    houseKeeping() 
    detailLoop()
    endOfJob()
    return


# call main
if __name__ == "__main__":
    main()

