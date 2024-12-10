import os

# Load all records into a Python list, called record, with \n removed and store different data as different list items with reference to the delimiter, i.e. semi-colon
def load_record():   # function with NO returned value
    # add your code here
    if os.path.exists("phonebook.txt"):    # school-based: check if the text file exists first
        f = open("phonebook.txt", "r")     # try to change to phonebook0.txt for testing empty text file
        global record
        record = f.readlines()
        if len(record) > 0:            # school-based: Check at least one record exists in the text file
            for i in range(0, len(record)):
                record[i] = record[i].replace("\n", "")
                record[i] = record[i].split(";")
            print("Phonebook.txt being imported successfully")
            f.close()
        else:
            print("Empty file with no records.")      # school-based: Output a prompt to the user for the empty file.   
    else:
        print("Non-existing file.")                    # school-based: Output a prompt to the user for the non-existing file.
    x = input("Press any key to be back to main menu ...")
    
def print_AllRecords():    # function with NO returned value
    # add your code here
    print()
    print("First Name" + "\t" + "Last Name" + "\t" + "No. Type" + "\t" + "Phone No.")     # "\t" denotes to insert a tab where this is suitable for display left-aligned data
    print("==========" + "\t" + "=========" + "\t" + "========" + "\t" + "=========")
    for i in range(0, len(record)):  
        for j in range(0, ??):                      # display 4 fields
            print(record[i][j], end = "\t\t")        # show data in a tabular format, i.e. columnar format
        print()
    x = input("Press any key to be back to main menu ...")

def print_SingleRecord(p):
# function with NO returned value and passing a parameter p indicating the index of the record to be printed
    # modify your code here
    print("First name:\t", record[p][0])
    print("Last name:\t", record[p][??])
    print("No. Type:\t", ??)
    print("Phone No.:\t", ??)
    x = input("Press any key to be back to main menu ...")

def add_record(firstname, lastname, noType, number):
# function with NO returned value and passing 4 parameters containing the data of the record to be added to the text file
    # modify the code below
    f = ??("phonebook.txt", ??)           # fill in a suitable mode of file handling for opening a text file for appending record to it
    f.??("\n" + firstname + ";" + lastname + ";" + noType + ";" + number)   # write a new line followed by a record containing data of different fields and the delimiter (i.e. semi-colon) to the text file
    ??                     # close the file
    ??()   # call an existing self-defined function for loading the most updated records from the text file to the current Python list
    print("1 record been saved to the text file successfully.")   # school-based: Output a prompt to the user for the successful saving 1 record to the file.
    print()
    x = input("Press any key to be back to main menu ...")

def update_record():   # function with NO returned value
    # add your code here
    print("1 record been updated and saved to the text file successfully.")    # school-based: Output a prompt to the user for the successful modificiation and saving 1 record to the file.
    print()
    x = input("Press any key to be back to main menu ...")
    
def searchRecord_ByFirstName(firstname):   # function with RETURNED VALUE
    # modify your code below
    for i in range(0, ?):
        if record[??][??] == firstname:
            return ??
    return ??                   # return a value if the first name cannot be found                                   
    

def deleteRecord_ByFirstName(firstname):     # function with NO returned value
   # add your code here
   print("1 record been deleted from the text file successfully.")    # school-based: Output a prompt to the user for the successful deletion 1 record from the file.
   print()
   x = input("Press any key to be back to main menu ...")

def deleteFile():     # function with NO returned value
    # add your code here
    filename = input("Enter a filename, such as phonebook.txt: ")    # backup the text file to be deleted to another place first
    if os.path.exists(filename):
        os.remove(filename)
        print("The file been removed successfully")       # school-based: Output a prompt to the user for the successful deletion 1 file.
    else:
        print("Non-existing file!")                          # school-based: Output a prompt to the user for the non-existing file.
    x = input("Press any key to be back to main menu ...")

def displayMainMenu():     # function with NO returned value
    print()
    print("Main Menu")
    print("1. Load records")
    print("2. Print all records")
    print("3. Add records")
    print("4. Update records")
    print("5. Search record by first name")
    print("6. Delete records")
    print("7. Delete file")    
    print("9. Exit")

# Main program
displayMainMenu()
print()
option = int(input("Press a number key to select an option: "))
while option != 9:
    match option:
        case 1: load_record()
        case 2: print_AllRecords()
        case 3:
                print()
                firstname = input("Enter first name: ")
                lastname = input("Enter last name: ")
                noType = input("Enter No. Type (Mobile/Home): ")
                number = input("Enter Phone Number: ")
                add_record(firstname, lastname, noType, number)
        case 4: update_record()
        case 5:
            print()
            fn = input("Enter first name to be searched: ")       # prompt user to ask for input
            if len(fn) > 0:
                p = searchRecord_ByFirstName(fn)
                if p == -1 :
                    print("Record not found")
                else:
                    print_SingleRecord(p)
            else:
                print("Operation aborted.  At least 1 character for inputting first name.")
        case 6: deleteRecord_ByFirstName(firstname)
        case 7: deleteFile()
    displayMainMenu()
    option = int(input("Press a number key to select an option: "))
print("Thank you for using this program. Bye!")
    