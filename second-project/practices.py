from time import sleep

def count_down(num):
    if num == 1:
        return num
    
    return f"{num}, {count_down(num-1)}"

def print_char_loop(string):
    for i, char in enumerate(string, start=1):
        print(f"{i}. {char}")

def password():
    pw = input("Set your password: ")
    correct = False
    tries = 0

    while not correct:
        user_input = input("Input your password: ")
        tries += 1
        if user_input == pw:
            print("Let's goooooooo. Correct")
            break
        elif user_input == "stop lol":
            print("Aight you can stop now.")
            break
        elif tries == 3:
            for sec in range(10, 0, -1):
                print("WRONG PASSWORD. YOU'RE PUNISHED")
                print(f"Try again in {sec} seconds")
                sleep(1)
            tries = 0
        else: 
            print(f"Incorrect. Try again. You have {3 - tries} try left")

def main():
    user_num = int(input("Enter a number: "))
    print(count_down(user_num))

    user_string = input("Enter a string: ")
    print_char_loop(user_string)

    password()

main()