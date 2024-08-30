import os # provides access to operating system-dependent functionality
import project_handler as ph # project handler module for creating and deleting projects
from colorama import init, Fore, Back, Style
import tkinter as tk # module for GUI
import machine_select


init() # colorama initialization

# folder path for project creation 
PROJECT_FOLDER_PATH, WEB_DEV_FOLDER_PATH = machine_select.select_machine()

count = 0 # count for invalid input attempts
exit = False

if os.path.isdir(PROJECT_FOLDER_PATH) == True or os.path.isdir(WEB_DEV_FOLDER_PATH) == True: # checks for valid project path

    print(Style.BRIGHT + Fore.GREEN + "\n[Practice Project Initializer]" + Style.RESET_ALL)

    while True:
        exit = False
        print(Style.DIM + "\nproject(s) path is valid." + Style.RESET_ALL) # confirmation message 
        folder_path_selection = input("\n[1] python\n[2] webdev\n[3] Exit\nSelect a path: ")

        # changes working directory to  specified project folder path
        if folder_path_selection == "1":
            os.chdir(PROJECT_FOLDER_PATH)
            # prints current working directory with desired style for text
            print(Style.DIM + "\nCurrent directory: " + os.getcwd() + Style.RESET_ALL)

            # loops if input is invalid prompting user input again 
            while exit == False:
                user_input = input("\n[1] Create a new project\n[2] Delete a project\n[3] Return to main selection\n[4] Exit\nSelect: ")
                
                # Validate user input
                if user_input == "1":  # Creates new project folder with main.py file
                    new_dir = input("\nProject name: ")
                    ph.create_project(new_dir)
                elif user_input == "2":  # Deletes existing project
                    os.chdir(PROJECT_FOLDER_PATH)
                    print("\nAvailable projects to remove:\n" + str(os.listdir('.')))
                    rm_dir = input("\nRemove project: ")
                    ph.delete_project(rm_dir)
                elif user_input == "3": # returns to main selection
                    exit = True
                    break
                elif user_input == "4": # Exits program
                    print("\nExiting...\n")
                    exit() # exit function
                else:  # Invalid input handling
                    print(Fore.RED + "\nInvalid input, please select a valid option" + Style.RESET_ALL)
                    count += 1
                    print(f"attempt: {count}\n")

                if count > 3:
                    os.system('cls')
                    count = 0

        elif folder_path_selection == "2":
            os.chdir(WEB_DEV_FOLDER_PATH)
            # prints current working directory with desired style for text
            print(Style.DIM + "\nCurrent directory: " + os.getcwd() + Style.RESET_ALL)

            while not exit:
                user_input = input("\n[1] Create a new project\n[2] Delete a project\n[3] Return to main selection\n[4] Exit\nSelect: ")

                if user_input == "1":
                    new_dir = input("\nProject name: ")
                    ph.create_webdevkit(new_dir)
                elif user_input == "2":
                    os.chdir(WEB_DEV_FOLDER_PATH)
                    print("\nAvailable projects to remove:\n" + str(os.listdir('.')))
                    rm_dir = input("\nRemove project: ")
                    ph.delete_project(rm_dir)
                elif user_input == "3":
                    exit = True
                    break
                elif user_input == "4": # Exits program
                    print("\nExiting...\n")
                    exit() # exit function
                else:
                    print(Fore.RED + "\nInvalid input, please select a valid option" + Style.RESET_ALL)
                    count +=1
                    print(f"attempt: {count}\n")

                if count > 3:
                    os.system('cls')
                    count = 0
        elif folder_path_selection == "3":
            print("\nExiting...\n")
            exit() # exit function
        else:
            print(Fore.RED + "\ninvalid input." + Style.RESET_ALL)
            count +=1 # counts each invalid input
            print(f"attempt: {count}\n") # prints attempt to console 
        
        # if invalid inputs exceed 3 attempts the screen is cleared and the user is prompted again, count is then set back to 0
        if count > 3:
            os.system('cls')
            count = 0
            


   # print(Style.RESET_ALL) # Resets to default
else:
    print(Style.DIM + Fore.RED + "ERROR, invalid path." + Style.RESET_ALL)


