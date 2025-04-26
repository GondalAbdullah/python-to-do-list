import os        # for managing directories and file
import csv       # for reading and writing to csv files
import hashlib   # for using secure-hashing-algorithm

credentials_file = os.path.join("user_data", "credentials.csv")

# hashing is the process of mapping data into fixed-length string of data
# takes password in the form of simple string and returns it in the form of secure hash
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest() # it converts the encoded string into a secure hash and then returns in the form of hex value




# ensures the presence of "user_data" directory and credential file
def create_credentials():
    os.makedirs("user_data", exist_ok=True) # creates "user_data" directory if it doesn't already exists
    if not os.path.exists(credentials_file): # creates "credentials" file if it doesn't alreadt exists
        try:
            with open(credentials_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["USERNAME", "HASHED PASSWORD"])  # Writing the header as first line
        except Exception as e:
            print(f"Error: {e}")




# takes in credentials, creates user's file and returns boolean value on the basis of correct sign-up
def sign_up(username, password, confirm_password):
    create_credentials()

    # Checking for existing username
    with open(credentials_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                print("Username already taken. Please choose a different one.")
                return False

    # Ensuring passwords match
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return False

    # Creating user's file
    tasks_file_path = os.path.join("user_data", f"{username}_tasks.csv")
    try:
        with open(tasks_file_path, mode="w", newline="") as u_file:
            writer = csv.writer(u_file)
            writer.writerow(["INDEX", "STATUS", "TITLE", "DESCRIPTION", "CATEGORY", "DEADLINE", "PRIORITY"])
    except Exception as e:
        print(f"Error: {e}")
        return False

    # Saving credentials
    hashed_password = hash_password(password)
    try:
        with open(credentials_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, hashed_password])
        print("Sign-up successful!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# takes credentials as arguments and returns bool value on the basis of correct login
def login(username, password):
    create_credentials()
    hashed_input_password = hash_password(password)

    with open(credentials_file, mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username: # checking for username
                if row[1] == hashed_input_password: # checking for password
                    print("Login successful!")
                    return True
                else:
                    print("Incorrect password.")
                    return False

    print("Username not found.")
    return False
