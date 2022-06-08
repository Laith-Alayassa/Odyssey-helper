
import pdfplumber
from dateutil.parser import parse
import os
import sys
import glob

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



wrong_inputs = ['Available:','Checked']


path_to_pdf = find_latest_file()
with pdfplumber.open(path_to_pdf) as pdf:
    for l,pg in enumerate(pdf.pages):
        page  = pdf.pages[l]
        text = page.extract_text()
    for row in text.split('\n'):
        row = row.split()

        try:
            if is_date(row[-4]) and row[0] not in wrong_inputs:
                due_date = row[-4]
                item_borrowed = ""
                student = ''
                # find student id its index in list
                for element in row:
                    if len(element) == 9 and element.isnumeric():
                        id_index = row.index(element)
                        id = element
                
                # find item name
                for i in range(0,id_index-1):
                    item_borrowed += row[i] + " "
                
                for i in range (id_index + 1, len(row) - 4):
                    student += row[i]
                    
                print(f'\n The student: {student}, id num: {id} borrowed {item_borrowed} that is due {due_date}')
                # print(row)
                print('\n')

        except:
            pass


