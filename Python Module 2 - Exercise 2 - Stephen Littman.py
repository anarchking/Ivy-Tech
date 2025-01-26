'''
Exercise 2
Using your course text, Title: Programming Logic & Design Edition: 10th.

Complete Chapter 2, Programming Exercise #8 on page 61. 
Draw the flowchart and design the logic for a program that calculates the projected cost of a remodeling project. 
Assume that the labor cost is $30 per hour. Design a program that prompts the user for a number of hours projected for the job and the wholesale cost of materials. 
The program computes and displays the cost of the job, which is the number of hours multiplied by the hourly rate plus 120 percent of the wholesale cost of materials.
Did it work?  Guess what? You just completed a testing scenario, which we will learn more about in future modules. 
'''

#initialization
LABOR = 30.00
WHOLESALE_TAX = 0.2
projectedHours = 0.0
laborCost = 0.00
wholesaleCost = 0.00
markup = 0.00
materialTotal = 0.00
totalCost = 0.00
switch = True


# process function where the computing happens
def process():
    global laborCost
    laborCost = projectedHours * LABOR
    global markup
    markup = wholesaleCost * WHOLESALE_TAX
    global materialTotal
    materialTotal = wholesaleCost + markup
    global totalCost
    totalCost = laborCost + materialTotal
    return


# breakDown function where all information is displayed
def breakDown():
    print("--- Projected Cost Breakdown ---")
    print(f"Labor Cost: ${laborCost:.2f}")
    print(f"Wholesale Cost of Materials: ${wholesaleCost:.2f}")
    print(f"Markup on Materials (120%): ${markup:.2f}")
    print(f"Total Material Cost: ${materialTotal:.2f}")
    print(f"Total Projected Cost: ${totalCost:.2f}")
    print("Projected cost calculation complete.")
    return


# end of program function
def endOfJob():
    print("The program has ended.")
    return


# clear previously saved values function
def zeroOut():
    projectedHours = 0.0
    laborCost = 0.00
    wholesaleCost = 0.00
    markup = 0.00
    materialTotal = 0.00
    totalCost = 0.00
    return


# main function
def main():
    while True:
        zeroOut()
        global projectedHours
        projectedHours = float(input("Please enter the number of hours projected for the job: "))
        if projectedHours == 0:
            break
        global wholesaleCost
        wholesaleCost = float(input("Please enter the material wholesale price: "))
        process()
        breakDown()
    endOfJob()
    return


# call main
if __name__ == "__main__":
    main()

