#Exercise 1: Movie Ticket Price Calculator

age = int(input("Enter your age: "))

if age <= 12:
    price = 5
elif age <=17:
    price = 8
elif age <=50:
    price = 12
else:
    price = 7

print(f"The ticket price is ${price}.")