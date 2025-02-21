def calculateExpenses(salary, month, savingPercent, rentPercent, electricityPercent):
    totalPercent = savingPercent + rentPercent + electricityPercent

    if totalPercent > 100:
        print("The totalPercent can't exceed 100%.Please re-enter the values.")
        return

    savings = (savingPercent * salary) / 100
    rent = (rentPercent * salary) / 100
    electricity = (electricityPercent * salary) / 100

    totalExpenses = savings + rent + electricity
    remindSalary = salary - totalExpenses
    yearlyRent = rent * 12
    yearlyElectricity = electricity *12
    squaredSalary = salary ** 2

    while True:
        try:
            additionalSavings = float(input("Enter your additional savings: "))
            if additionalSavings < 0:
                print("Amount can't be negative.Please enter a valid number")
                continue
            break
        except ValueError:
            print("Invalid input.Please enter a numeric value")

    if savings > 0:
        extraSavings = additionalSavings / savings
    else:
        0

    print("========Monthly Finances========")
    print(f"Salary: {salary}$")
    print(f"Month: {month}")
    print(f"Savings: {savings}$")
    print(f"Rent: {rent}$")
    print(f"Electricity: {electricity}$")
    print(f"Total Expenses: {totalExpenses}$")
    print(f"Remind Salary: {remindSalary}$")
    print(f"Yearly Rent: {yearlyRent}$")
    print(f"Yearly Electricity: {yearlyElectricity}$")
    print(f"Salary Squared: {squaredSalary}$")
    print(f"Remaining after additional savings of {additionalSavings}$ : {extraSavings}")

while True:
    userInput = input("Type 'exit' to quit or prees Enter to continue: ")
    if userInput == "exit":
        break
    try:
        salary = float(input("Enter Salary: "))
        print(f"Nabiha's Salary {salary}$")

        month = str(input("Enter the name of the month: ")).capitalize()

        savingPercent = float(input("Enter the percentages for Savings: "))
        print(f"Savings: {savingPercent}%")

        rentPercent = float(input("Enter the percentages for Rent: "))
        print(f"Rent: {rentPercent}%")

        electricityPercent = float(input("Enter the percentages for Electricity: "))
        print(f"Electricity: {electricityPercent}%")


        calculateExpenses(salary, month, savingPercent, rentPercent, electricityPercent)
    except ValueError:
        print("Enter a valid number")