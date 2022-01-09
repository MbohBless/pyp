"""
the following project is a python project which is very useful is task automation
specifically in this case the program receives a file in the csv format which is then
read and then the emails are then updated to the desired level of work or text
the code is explained in details on each step
these two lines handles the imports which are the csv
 and the pandas library. these which individually handle different task. the csv handles
  the csv writers which will ease the writing information into a csv file while the pandas library will ease
  the detailed reading of the csv or xlsx file in the case if any are being used"""

import pandas as pd
import os

# the storage path of the given file which needs to be edited
read_path = 'input/employeedata.csv'
read_path_excel = 'input/employeedata.xlsx'

# # this is the storage path of the given output file once
write_path = 'output/updated_employee_data.csv'
write_path_xl = 'output/updated_employee_data.xlsx'


# modification is complete


# this function deals with actually retrieving the csv file from its original state.
def fetch_csv():
    employee_details = pd.read_csv(read_path)
    return employee_details


def fetch_excel():
    employee_details = pd.read_excel(read_path_excel)
    return employee_details


# this function handles the getting the individual columns into list for easy data manipulation
def read_details():
    data_file = None
    # this is a file checker to know if the given path is available and then fetches the else uses the other path
    if os.path.exists(read_path):
        data_file = fetch_csv()
    else:
        data_file = fetch_excel()
    old_email = data_file["Email"].tolist()
    new_emails = []
    names = data_file["Name"].tolist()
    phone = data_file["Phone"].tolist()
    for email in old_email:
        """.replace() is a prebuilt python string operation function which helps to replace a 
        specified piece of string or character with another provided"""
        new_emails.append(email.replace("@helpinghands.cm", "@handsinhands.org"))
    print(".....")
    create_updated_csv(names, new_emails, phone)


# this function handles the creation and writing of the updated email file
def create_updated_csv(names, new_emails, phone):
    # conversion of list into a dictionary to make it fit for placing them into the csv file properly
    my_dict = {"Name": names, "Email": new_emails, "Phone": phone}
    df = pd.DataFrame(my_dict)
    print("1. csv\n2. xlsx")
    choice = None
    """ cast check if the variable is possible to convert to int
    this is a try catch block which is essential to the function or producing the output but this 
    in case of wrong number is choosen then it sigals o the individual that wrong input
    """
    try:
        choice = int(input("enter desired format;"))
    except ValueError:
        print(" wrong choice; enter a number corresponding to each")
    # this path is used to chose an option to handle if to return a csv or an xlsx file
    if choice == 1:
        df.to_csv(write_path)

    elif choice == 2:
        df.to_excel(write_path_xl)
    else:
        print("wrong choice")


# general function call which might be or not used
def update_emails():
    read_details()


# specifically using this way of running the project to ensure that in case the program becomes large and has
# many runnable parts then it will be easy to specify
if __name__ == '__main__':
    # general function called here for operation
    update_emails()
