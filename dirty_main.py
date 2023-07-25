from application.salary import *
from application.db.people import * 
import datetime as dt 

if __name__ == '__main__':
    print(dt.date.today())
    print(calculate_salary())
    print(get_employees())