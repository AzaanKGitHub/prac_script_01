import os

webdev = None
python = None

def select_machine():
    machine_name = os.environ.get('COMPUTERNAME', os.environ.get('HOSTNAME', 'Unknown'))
    print(f"\nMachine: {machine_name}")

    if machine_name == "DESKTOP-T70FFL4":
        python = "C:\\Users\\Azaan\\OneDrive\\Desktop\\Python"
        webdev = "C:\\Users\\Azaan\\OneDrive\\Desktop\\Webdev"
    elif machine_name == "LENOVO_THINKPAD":
        python = "C:\\Users\\Lenovo\\Desktop\\python\\practice"
        webdev = "C:\\Users\\Lenovo\\Desktop\\webdev\\practice"
    else:
        print("\nInvalid selection.")

    return python, webdev # returns python and webdev path variables