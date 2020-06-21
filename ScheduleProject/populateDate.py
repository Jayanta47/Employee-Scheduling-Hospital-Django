import os
import random

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ScheduleProject.settings')

django.setup()

from datetime import date, timedelta
from firstapp.models import DimDate, DimEmployee
from faker import Faker

def populatedate():
    s_date = date(2020, 6, 20)
    e_date = date(2020, 12, 31)

    delta = e_date - s_date

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    dayI = 0
    for i in range(delta.days + 1):
        day = s_date + timedelta(days=i)
        hol = False
        weknd = False
        if (dayI + i) % 7 == 6:
            hol = True
            weknd = True
        # print(str(day) + " " + days[(dayI + i) % 7])
        d = DimDate(keyDate=i + 1, FullDate=day, dayOfWeek=days[(dayI + i) % 7], dayInWeek=(dayI + i) % 7 + 1,
                    isHoliday=hol, isWeekend=weknd)
        d.save()


def deleteDate(serial):
    for i in range(serial):
        DimDate.objects.filter(keyDate=i+1).delete()


def sortEntry():
    DimDate.objects.order_by('keyDate')


def populateemployee(N = 10):
    random.seed(0)
    Faker.seed(0)
    fake = Faker()
    jobs = ["Doctor", "Nurse/Ward Boy", "Manager", "Web Administrator", "Technician", "Receptionist"]

    for i in range(N):
        num = random.randint(0, 5)
        d = DimEmployee(empId=i+1, firstName=fake.first_name(), lastName= fake.last_name(), status=jobs[num])
        d.save()


if __name__ == '__main__':
    # populateemployee(30)
    populatedate()
    print("populated successfully")