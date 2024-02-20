from datetime import date

from application import salary
from application.db import people

from cowsay import cowsay

def cow_say(message):
    print(cowsay(message))



if __name__ == '__main__':
    print(date.today())
    print(people.get_employees())
    print(salary.calculate_salary())
    cow_say("Вот это Бухгалтерия!")