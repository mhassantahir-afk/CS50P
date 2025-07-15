from datetime import date
from datetime import datetime
import re
import inflect
import sys

p = inflect.engine()

class takestr:
    def __init__(self, bdate, tdate):
        self.bdate = bdate
        self.tdate = tdate


    def __str__(self):
        diff_date = self.tdate - self.bdate
        if diff_date.days > 0:
            return f"{p.number_to_words((diff_date.days)*1440, andword="").capitalize()} minutes"
        else:
            print("Invalid date")
            sys.exit(1)

    @property
    def bdate(self):
        return self._bdate

    @bdate.setter
    def bdate(self, bdate):
        self._bdate = check_date(bdate)

    @property
    def tdate(self):
        return self._tdate

    @tdate.setter
    def tdate(self, tdate):

        self._tdate = check_date(tdate)

def get_date():
    bdate = input("Date of Birth: ")
    tdate = str(date.today())
    return takestr(bdate, tdate)

def check_date(gdate):
    if match := re.search(r"^([0-9][0-9][0-9][0-9])\-((0[0-9])|(1[0-2]))\-(([0-2][0-9])|(3[0-1]))$", gdate):
            return datetime.strptime(gdate, "%Y-%m-%d").date()
    else:
        print("Invalid date")
        sys.exit(1)

def main():
    _date = get_date()
    print(_date)


if __name__ == "__main__":
    main()
