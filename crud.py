import utils                    # for using input validation function
import csv                      # for reading and writing to csv files
import os                       # for managing the existing of directories
from tabulate import tabulate   # for outputing csv files on console in a tabular form
import datetime                 # for maniputing with dates


# returns the path to user's task file
def path_to_dir(username):
    return os.path.join("user_data", f"{username}_tasks.csv")




# def create_tasks_csv(username, category_name):
#     file_path = os.path.join("user_data", username, f"{username}_{category_name}.csv")
    
#     os.makedirs(os.path.dirname(file_path), exist_ok=True)
#     if not os.path.exists(file_path):
#         with open(file_path, mode='w', newline='', encoding='utf-8') as c_file:
#             writer = csv.writer(c_file)
#             writer.writerow(["INDEX", "STATUS", "TITLE", "DESCRIPTION", "DEADLINE", "PRIORITY"])



# returns total number of entries to assign it to the latest entry
def number_of_rows(file_path):

    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        total_rows = sum(1 for row in reader)

    return total_rows



# updates the index of entries when an entry is deleted or updated
def update_list_index(file_path):
    updated_rows = []

    with open(file_path, mode='r', newline='') as rfile:
        reader = csv.DictReader(rfile)
        fieldnames = reader.fieldnames
        curr_index = 1

        for row in reader:
            row["INDEX"] = str(curr_index)
            updated_rows.append(row)
            curr_index += 1

    with open(file_path, mode='w', newline='') as wfile:
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)



# updates the priority of entries in order of priority when an entry is deleted or updated
def update_file_priority(file_path):

    with open(file_path, mode='r', newline='') as rfile:
        reader = csv.DictReader(rfile)
        fieldnames = reader.fieldnames

        # Separate rows by priority
        high_priority = []
        medium_priority = []
        low_priority = []

        for row in reader:
            priority = row["PRIORITY"].lower()
            if priority == "high":
                high_priority.append(row)
            elif priority == "medium":
                medium_priority.append(row)
            else:
                low_priority.append(row)

        # Combine rows in the desired order
        sorted_rows = high_priority + medium_priority + low_priority

    with open(file_path, mode='w', newline='') as wfile:
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_rows)



# removes all the tasks whose deadlne has passed
def remove_expired_tasks(file_path):
    updated_rows = []

    # Get the current date of today
    today = datetime.date.today()

    with open(file_path, mode='r', newline='') as rfile:
        reader = csv.DictReader(rfile)
        fieldnames = reader.fieldnames

        for row in reader:
            try:
                deadline_date = datetime.datetime.strptime(row["DEADLINE"], "%Y-%m-%d").date()
                if deadline_date >= today:  # Keep tasks with deadlines today or in the future
                    updated_rows.append(row)
            except Exception as e:
                print(f"Error: {e}")

    with open(file_path, mode='w', newline='') as wfile:
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)



#########################################################################



# outputs all the tasks in a tabular manner using 'tabulate' library
def show_all_tasks(username):
    
    try:
        with open(path_to_dir(username), mode='r', newline='') as rfile:
            reader = csv.reader(rfile)
            data = list(reader)
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
    except Exception as e:
        print(f"Error: {e}")

    print()




# updates the status of an etnry from pending to completed
def mark_task_done(target_index, username):
    rows_to_update = []

    with open(path_to_dir(username), mode='r', newline='') as rfile:
        reader = csv.DictReader(rfile)
        fieldnames = reader.fieldnames
        
        for row in reader:
            if row["INDEX"] == target_index:
                row["STATUS"] = "completed"
            rows_to_update.append(row)
        
    index_found = any(row["INDEX"] == target_index for row in rows_to_update)
    
    if not index_found:
        print(f"No task found with index {target_index}.")
        return
    else:
        with open(path_to_dir(username), mode='w', newline='') as wfile:
            writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_to_update)


# enters new task to the user's file
def enter_new_task(username, task_title, task_description, task_category, task_due_date, task_priority):

    with open(path_to_dir(username), mode='a', newline='') as file:
        writer = csv.writer(file)

        try:
            due_date = datetime.date.today() + datetime.timedelta(days=int(task_due_date))
            writer.writerow([number_of_rows(path_to_dir(username)), "pending", task_title, task_description, task_category, due_date, task_priority])
        except Exception as e:
            print(f"Error: {e}")

    update_file_priority(path_to_dir(username))
    update_list_index(path_to_dir(username))

    print("\nTask added successfully.\n")



# updates any column of the entries you want
def update_task(target_index, username):
    rows_to_update = []

    # Read the existing tasks and check if the target index exists
    with open(path_to_dir(username), mode='r', newline='') as rfile:
        reader = csv.DictReader(rfile)
        fieldnames = reader.fieldnames

        for row in reader:
            rows_to_update.append(row)
    
    # Check if the target index exists
    target_row = next((row for row in rows_to_update if row["INDEX"] == target_index), None)
    if not target_row:
        print(f"No task found with index {target_index}.")
        return

    # inputing values to update or not
    new_title = input(f"Enter new title (or 'na' to keep as '{target_row['TITLE']}'): ")
    new_description = input(f"Enter new description (or 'na' to keep as '{target_row['DESCRIPTION']}'): ")
    new_category = input(f"Enter new category (or 'na' to keep as '{target_row['CATEGORY']}'): ")
    new_days_to_expiry = input(f"Enter new days to expiry (or 'na' to keep as '{target_row['DEADLINE']}'): ")
    priority_input = utils.validate_input(f"Enter new priority ('1' for HIGH, '2' for MEDIUM, '3' for LOW or 'na' to keep as '{target_row['PRIORITY']}'): ", "^(1|2|3|na)$")

    # dealing with 'na' values
    target_row["TITLE"] = new_title if new_title.lower() != "na" else target_row["TITLE"]
    target_row["DESCRIPTION"] = new_description if new_description.lower() != "na" else target_row["DESCRIPTION"]
    target_row["CATEGORY"] = new_category if new_category.lower() != "na" else target_row["CATEGORY"]

    if new_days_to_expiry.lower() != "na":
        try:
            days_to_expiry = int(new_days_to_expiry)
            target_row["DEADLINE"] = (datetime.date.today() + datetime.timedelta(days=days_to_expiry)).strftime("%Y-%m-%d")
        except Exception as e:
            print("Invalid number. Keeping the original due date.")
    else:
        target_row["DEADLINE"] = target_row["DEADLINE"]

    if priority_input == '1':
        new_priority = "High"
    elif priority_input == '2':
        new_priority = "Medium"
    elif priority_input == '3':
        new_priority = "Low"
    else:
        new_priority = target_row["PRIORITY"]
    target_row["PRIORITY"] = new_priority if new_priority.lower() != "na" else target_row["PRIORITY"]

    with open(path_to_dir(username), mode='w', newline='') as wfile:
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows_to_update)

    update_file_priority(path_to_dir(username))
    update_list_index(path_to_dir(username))

    print("\nTask updated successfully.\n")



def delete_task(target_index, username):
    updated_rows = []
    entry_found = False
    show_all_tasks(path_to_dir(username))

    with open(path_to_dir(username), mode='r', newline='') as rfile:
        reader = csv.DictReader(rfile)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["INDEX"].strip() == str(target_index).strip():
                entry_found = True
                # skipping the specified entry so the file doesn't store it again
                continue
            updated_rows.append(row)


    if not entry_found:
        print(f"No entry found with index {target_index}.")
        return

    with open(path_to_dir(username), mode='w', newline='') as wfile:
        writer = csv.DictWriter(wfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    update_list_index(path_to_dir(username))

    print("\nTask deleted successfully.\n")