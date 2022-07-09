
from datetime import date
from dateutil.parser import parse

today = date.today().strftime("%d/%m/%Y")
today = parse(today)
def is_late(item_date, today):
    item_due = parse(item_date)
    print(f"the item is late {item_due >= today}")


is_late("09/07/2022", today)
