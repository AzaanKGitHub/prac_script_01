import os # provides access to operating system-dependent functionality
import project_handler as ph # project handler module for creating and deleting projects
from colorama import init, Fore, Back, Style
import tkinter as tk # module for GUI 

# folder path for project creation 
PROJECT_FOLDER_PATH = "C:\\Users\\Lenovo\\Desktop\\python\\practice"
WEB_DEV_FOLDER_PATH = "C:\\Users\\Lenovo\\Desktop\\webdev\\practice"
count = 0 # count for invalid input attempts

if os.path.isdir(PROJECT_FOLDER_PATH) == True or os.path.isdir(WEB_DEV_FOLDER_PATH) == True: # checks for valid project path
    print(Style.DIM + "project(s) path is valid." + Style.RESET_ALL) # confirmation message 

    print(Style.BRIGHT + Fore.GREEN + "\n[Practice Project Initializer]\n" + Style.RESET_ALL)

    while True:
        folder_path_selection = input("[1] python\n[2] webdev\nSelect a path: ")

        # changes working directory to  specified project folder path
        if folder_path_selection == "1":
            os.chdir(PROJECT_FOLDER_PATH)
            # prints current working directory with desired style for text
            print(Style.DIM + "\nCurrent directory: " + os.getcwd() + Style.RESET_ALL)

            # loops if input is invalid prompting user input again 
            while True:
                user_input = input("\n[1] Create a new project\n[2] Exit program\n[3] Delete a project\nSelect: ")
                
                # Validate user input
                if user_input == "1":  # Creates new project folder with main.py file
                    
                    new_dir = input("\nProject name: ")
                    ph.create_project(new_dir)
                elif user_input == "2":  # Exits program
                    print("\nExiting...\n")
                    exit() # exit function
                elif user_input == "3": # Deletes existing project
                    os.chdir(PROJECT_FOLDER_PATH)
                    print("\nAvailable projects to remove:\n" + str(os.listdir('.')))
                    rm_dir = input("\nRemove project: ")
                    ph.delete_project(rm_dir)
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

            while True:
                user_input = input("\n[1] Create a new project\n[2] Exit program\n[3] Delete a project\nSelect: ")

                if user_input == "1":
                    new_dir = input("\nProject name: ")
                    ph.create_webdevkit(new_dir)
                elif user_input == "2":
                    print("\nExiting...")
                    exit()
                elif user_input == "3":
                    os.chdir(WEB_DEV_FOLDER_PATH)
                    print("\nAvailable projects to remove:\n" + str(os.listdir('.')))
                    rm_dir = input("\nRemove project: ")
                    ph.delete_project(rm_dir)
                else:
                    print(Fore.RED + "\nInvalid input, please select a valid option" + Style.RESET_ALL)
                    count +=1
                    print(f"attempt: {count}\n")

                if count > 3:
                    os.system('cls')
                    count = 0
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


