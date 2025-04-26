# To-Do List Application (Python Project)

This is a simple **command-line To-Do List Application** built with Python.  
The app allows users to **sign up**, **log in**, and **manage their personal tasks**, with each user's data stored separately for security and easy tracking.

---

## Project Description

This project simulates a real-world **To-Do List Manager** with **user authentication**.  
Each user can:
- Sign up with a username and password
- Log in securely
- Create, view, update, and delete tasks
- Tasks are saved in individual CSV files for each user
- User credentials are stored securely in a central `credentials.csv` file

This modular structure uses **separate files** for different purposes to keep the project clean and maintainable.

---

## Project Structure

| File | Description |
|:---|:---|
| `main.py` | Main application file that runs the overall program and user interface. |
| `utils.py` | Helper functions for input validation, file handling, and general utilities. |
| `crud.py` | CRUD (Create, Read, Update, Delete) operations related to tasks. |
| `logins.py` | User authentication functions for sign-up and login handling. |
| `credentials.csv` | Stores usernames and hashed passwords (or plain text depending on your implementation) in `user_data` directory. |
| `[username]_tasks.csv` | Individual task files for each user to store their to-do items in `user_data` directory. |

---

## Features

- **User Authentication**
  - Sign-up with unique username
  - Log-in with username and password
- **Task Management**
  - Add new tasks
  - View all tasks
  - Update tasks
  - Delete tasks
- **Data Persistence**
  - Tasks saved separately for each user in their own CSV file
  - Credentials stored in a single CSV file
- **User-friendly command-line interface**

---

## Technologies Used

- Python 3
- tabulate
- CSV File Handling (`csv` module)
- Basic File Management (`os` module)

---

## How to Run

1. Make sure you have Python installed (version 3.6+ recommended).
2. Install tabulate library from pip.
3. Clone the repository or download the project files.
4. Open your terminal or command prompt.
5. Navigate to the project directory.
6. Run the application:
   ```
   python main.py
   ```
7. Follow the on-screen instructions to sign up, log in, and manage your tasks.

---

## Notes

- I used `msvcrt` to use `getch()` function for windows terminal. use `termios` if you have a linux or mac system.
- Each user's tasks are stored separately as `username_tasks.csv` to maintain user privacy.
- If `credentials.csv` or a user's task file does not exist, it will be created automatically.
- Make sure all Python files (`main.py`, `utils.py`, `crud.py`, `logins.py`) are in the same directory.

