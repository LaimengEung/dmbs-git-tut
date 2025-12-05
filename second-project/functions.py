def us_to_eu_floor(floor):
    if floor <= 0:
        return "How many kids in yo basement lmao."
    elif floor == 1:
        return "It's actually ground floor, stop being weird."
    elif floor < 14:
        return f"It's actually ground {floor-1} in Europe"
    else:
        return f"It's actually ground {floor-2} in Europe"

def us_to_eu_ternary(floor):
    return floor-1 if floor < 14 else floor-2

def print_row(number, order):
    return f"{number} x {order} = {number*order}"

def multi_table_recursive(number, order=1):
    if order > 10:
        return
    
    print(print_row(number, order))
    return multi_table_recursive(number, order+1)

def main():
    # us_floor = int(input("Yo American, what floor you want: "))
    # print(us_to_eu_ternary(us_floor))

    mul_num = int(input("What number you wanna see in da table: "))
    # multiplication_table(mul_num)
#    print( multi_recursive(10))
    multi_table_recursive(mul_num)
if __name__ == "__main__":
    main()