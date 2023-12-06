def openfiles():
    """
    Prompts the user for the file names to open, opens the file, and append it to the file list.
    If the file is not found, print "(file name) not found."
    Ask if the user wants to open more files. If the user doesn't want to open more files,
    stop getting user input and return file list.
    
    """

    #init
    terminate = False
    fileList = []

    while not terminate:
        filename = input("Enter 'file name.csv': ")

        try:
            file = open(filename, 'r', encoding='UTF8')
            fileList.append(file)
            print(f"{filename} opened successfully.")
            terminate = stop()

        except IOError:
            print(f"{filename} doesn't exist.")
            terminate = stop()

    return fileList


def openfiles_cp949():

    #init
    terminate = False
    fileList = []

    while not terminate:
        filename = input("Enter 'file name.csv': ")

        try:
            file = open(filename, 'r', encoding='cp949')
            fileList.append(file)
            print(f"{filename} opened successfully.")
            terminate = stop()

        except IOError:
            print(f"{filename} doesn't exist.")
            terminate = stop()

    return fileList


def stop():
    """
    Ask the user if he wants to input more files.
    If the user inputs Y or y, return False. Else, return True.
    """
    stop = input("Do you want to open more files?(Y/N) ")
    if stop in 'Nn':
        return True
    elif stop in 'Yy':
        return False
    else:
        print("Invalid input. Stop getting input")
        return True







