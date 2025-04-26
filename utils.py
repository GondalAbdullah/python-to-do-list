import re      # for using regular expressions in input validation
import msvcrt  # for using getch() function

# takes in input on the base of prompt and returns the user-input only when it matches the regex pattern
def validate_input(prompt, pattern):
    
    while True:
        user_input = input(prompt).strip() # strips the input if any whitespace is found
        if re.match(pattern, user_input): 
            return user_input.lower()  # Return the input in lowercase ('y' or 'n')
        else:
            print("Invalid input....\n")


# takes in plain string input but outputs a series of astericks on console(only works with windows consoles)
def input_password(prompt):
    print(prompt, end="", flush=True) # end ensures that input stays on the same line while flush keeps prompt without delay
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b'\r', b'\n'}:  # Enter key pressed
            print()  # Move to the next line
            break
        elif char == b'\x08':  # Backspace key pressed
            if len(password) > 0:
                print("\b \b", end="", flush=True)  # Erase the last '*'
                password = password[:-1]
        else:
            print("*", end="", flush=True) # appending '*' to console, whilst keeping on the same line without using input buffer
            password += char.decode()
    return password


