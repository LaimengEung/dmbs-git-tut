# Num Range
def num_range(num):
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print("You input 0 lol")

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is leap year")
    else: 
        print(year, "is not a leap year my bro.")

def calculator(num1, num2, op):
    ops = ['+', '-', '*', '/']
    if op == ops[0]:
        print(num1+num2)
    elif op == ops[1]:
        print(num1-num2)
    elif op == ops[2]:
        print(num1*num2)
    elif op == ops[3]:
        if num2 == 0:
            print("nah cannot divide by 0 lmao")
        else:    
            print(num1/num2)
    else:
        print(op, "aint a real operator lol")

def ticket_pricing(people_list):
    total = 0
    for age in people_list:
        if age < 12:
            total += 5
        elif age <= 65:
            total += 10
        elif age > 65:
            total += 7
    
    return total

def main():
    # Number Range
    print("Check if yo number pos, neg, or 0")
    print("=" * 40)
    user_num = int(input("Enter a number: "))
    num_range(user_num)

    # Leap Year
    print("\nCheck if yo year is leap or not")
    print("=" * 40)
    user_year = int(input("Enter your year: "))
    leap_year(user_year)

    # Calculator
    print("\nCalculator")
    print("=" * 40)
    ope = input("What calculation you wanna do: ")
    n1 = int(input("Enter 1st number: "))
    n2 = int(input("Enter 2nd number: "))
    calculator(n1, n2, ope)

    # Ticket Pricing
    print("\nTicket Pricing")
    print("=" * 40)
    tickets = int(input("How many ticket you want: "))
    peep_list = []
    for i in range(tickets):
        age = int(input(f"how old is person {i+1}: "))
        peep_list.append(age)

    print(f"Total Cost: {ticket_pricing(peep_list)}")

if __name__ == "__main__":
    main()