
import pdfplumber
from dateutil.parser import parse

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

with pdfplumber.open('items.pdf') as pdf:
    page  = pdf.pages[1]
    text = page.extract_text()
for row in text.split('\n'):
    row = row.split()

    try:
        if is_date(row[-4]):
            due_date = row[-4]
            item_borrowed = ""
            student = ''
            # find student id its index in list
            for element in row:
                if len(element) == 9 and element.isnumeric():
                    id_index = row.index(element)
                    id = element
            
            # find item name
            for i in range(0,id_index-2):
                item_borrowed += row[i] + " "
            
            for i in range (id_index + 1, len(row) - 4):
                student += row[i]
                
            print(f'\n The student: {student}, id num: {id} borrowed {item_borrowed} that is due {due_date} \n')

    except:
        pass
