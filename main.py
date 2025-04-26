import crud
import logins
import utils
import os


if __name__ == "__main__":

    login_check = True
    login_option = ""

    while login_check:
        print("1.Login    2.Signup    3.Exit\n")
        login_option = input("Enter preferred option: ")

        if login_option == "1":
            username = input("Enter your username: ")
            password = utils.input_password("Enter your password: ")
            if logins.login(username, password):
                print()

                main_menu_check = True                
                main_menu_option = ""



                while main_menu_check:
                    if os.path.exists(crud.path_to_dir(username)):
                        crud.remove_expired_tasks(crud.path_to_dir(username))
                        # crud.sign_almost_due_tasks(crud.path_to_dir(username))
                    crud.show_all_tasks(username)
                    print("1.Show tasks    2.Mark a task done    3.Enter new task    4.Update task    5.Delete task    6.Logout\n")
                    main_menu_option = input("Enter preferred option: ")

                    if main_menu_option == "1":
                        crud.show_all_tasks(username)

                    elif main_menu_option == "2":
                        curr_index = input("Enter index of preferred task: ")
                        crud.mark_task_done(curr_index, username)

                    elif main_menu_option == "3":
                        task_title = input("Enter task title: ")
                        task_description = input("Enter task description: ")
                        task_due_date = float(input("Enter days into expiry: "))


                        category_option = utils.validate_input("Do you want to add a category(enter 'y' for yes and 'n' for no): ", r'^[ynYN]$')
                        if category_option in ['y', 'Y']:
                            task_category = input('Enter desired category: ')
                        else:
                            task_category = 'others'

                        priority_option = utils.validate_input("Enter Priority('1' for HIGH, '2' for MEDIUM or '3' for LOW):", r'^[123]$')
                        if priority_option == '1':
                            task_priority = "High"
                        elif priority_option == '2':
                            task_priority = "Medium"
                        else:
                            task_priority = "Low"
                        crud.enter_new_task(username, task_title, task_description, task_category, task_due_date, task_priority)
                        
                    elif main_menu_option == "4":
                        
                        # crud.show_all_tasks(tasks_file_path)
                        curr_index = input("Enter index of preferred task: ")
                        # curr_title = input("Enter new title to update: ")
                        # curr_description = input("Enter new description to update: ")
                        # curr_category = input("Enter category to change: ")
                        # curr_date = int(input("Enter new day to expiry: "))

                        crud.update_task(curr_index, username)
                        

                    elif main_menu_option == "5":
                        
                        curr_index = input("Enter index of preferred task: ")
                        crud.delete_task(curr_index, username)
                        

                    elif main_menu_option == "6":
                        main_menu_check = False
                        print()

                    else:
                        print("Enter a valid option...\n")
            
            else:
                print("Incorrect Credentials\n")
        
        elif login_option == "2":
            username = input("Enter Username: ")
            password = utils.input_password("Enter password: ")
            confirm_password = utils.input_password("Confirm Password: ")
            logins.sign_up(username, password, confirm_password)
        elif login_option == "3":
            login_check = False
            print()
        
        else:
            print("Enter a valid option...\n")