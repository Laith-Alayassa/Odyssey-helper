
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
            date = row[-4]
            for item in row:
                if len(item) == 9 and item.isnumeric():
                    id = item
            # print(row)
            print(f"this is the id {id} and this is date {date} ")
            # print(f"row 3 is {row[-6]} and date is {row[-4]}")
    except:
        pass
