
import pdfplumber
from dateutil.parser import parse
import os
import sys
import glob
from pprint import pprint
from datetime import date


def find_latest_file():
    """finds the last file to be added to a folder (currently downloads folder)

    Returns:
        string: file path
    """
    list_of_files = glob.glob('/Users/laithalayassa/Downloads/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def is_late(item_date, today):
    """
    returns True of item is late

    item_date (string): date to return item
    today (string): today's date
    """
    item_due = parse(item_date)
    return item_due >= today


def find_late(path_to_pdf = ""):
    late_students = {}
    wrong_inputs = ['Available:', 'Checked']
    today = date.today().strftime("%d/%m/%Y")
    today = parse(today)

    if not path_to_pdf:  path_to_pdf = find_latest_file() 
    with pdfplumber.open(path_to_pdf) as pdf:
        for l, pg in enumerate(pdf.pages):
            page = pdf.pages[l]
            text = page.extract_text()
        for row in text.split('\n'):
            row = row.split()

            try:
                # Some names are too long and intersect with the date (eg. Alonso03/04/2002)
                # So I use the last 10 chars which are the the date
                date_location = row[-4][-10:]
                if is_date(date_location)  and row[0] not in wrong_inputs: #TODO: Add is late
                    due_date = row[-4]
                    item_borrowed = ""
                    student_name = ''
                    # find student id its index in list
                    for element in row:
                        # finds ID based on length and type
                        if len(element) == 9 and element.isnumeric():
                            id_index = row.index(element)
                            student_id = element

                    # find item name
                    for i in range(0, id_index - 1):
                        item_borrowed += row[i].replace('Checked', '')

                    # finds student name
                    for i in range(id_index + 1, len(row) - 4):
                        student_name += row[i]

                    # print(f'\n The student: {student_name}, id num: {student_id} borrowed {item_borrowed} that is due {due_date}')
                    # print('\n')
                    late_students[student_id] = [item_borrowed, student_name, due_date]
            except:
                pass
    return late_students


# print(find_late())
def write_emails(pdf_file = None):
    message = """Hello,

You checked out {} on {} and have not yet returned it to the hall office. This item is now overdue.

Please return it to the Dupre Hall Office immediately when the office is open. Hall office hours are listed below. A staff member needs to be present in the office when you turn the items in, otherwise it will be an improper check-in and you can still be charged a fee.
If the office is closed you can also call the RA on Duty from 7pm-8am, 7 days a week. 

As a reminder, if {} is not returned immediately when the office is open, you will be charged a replacement fee. 
If you have any further questions or you feel that you have received this email in error please feel free to contact RHD Samantha at syang9@macalester.edu 

Best, 
Dupre Office"""
    
    
    
    
    late_students = find_late(pdf_file)
    for student in late_students:
        message = message.format(late_students[student][0],late_students[student][-1], late_students[student][0])
        # Adds the email as the last element in dictionary, now it looks like {ID : [ITEM, NAME, Due-Date, Emailmessage]}
        late_students[student] = late_students[student] + [message]
    return late_students





if __name__ == '__main__':
    # This code won't run if this file is imported.
    write_emails()