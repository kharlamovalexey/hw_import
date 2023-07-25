import datetime as dt 
from application.salary import *
from application.db.people import * 

if __name__ == '__main__':
    print(dt.date.today())
    print(calculate_salary())
    print(get_employees())
