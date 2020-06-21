from django.db import models

# Create your models here.


class DimDate(models.Model):
    keyDate = models.IntegerField(primary_key= True, unique= True)
    FullDate = models.DateField()
    dayOfWeek = models.CharField(max_length=10)
    dayInWeek = models.IntegerField()
    isHoliday = models.BooleanField()
    isWeekend = models.BooleanField()

    def __str__(self):
        return str(self.FullDate) + " " + str(self.dayOfWeek)


class DimEmployee(models.Model):
    empId = models.PositiveIntegerField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    status = models.CharField(max_length=15)

    def __str__(self):
        return str(self.firstName) + " " + str(self.lastName) + " :" + str(self.status)


class TimeTable(models.Model):
    timeId = models.IntegerField(primary_key=True, unique=True)
    startTime = models.TimeField()
    endTime = models.TimeField()
    category = models.CharField(max_length=25)

    def __str__(self):
        return str(self.startTime) + " to " + str(self.endTime) + " category: " + str(self.category)


class Schedule(models.Model):
    scheduleId = models.IntegerField(unique=True, primary_key=True)
    keyDate = models.ForeignKey(DimDate, on_delete=models.CASCADE)
    employee = models.ForeignKey(DimEmployee, on_delete=models.CASCADE)
    shift = models.ForeignKey(TimeTable, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.keyDate) + " " + str(self.employee)
