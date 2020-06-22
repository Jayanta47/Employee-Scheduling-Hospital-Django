from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from firstapp.models import DimEmployee, TimeTable, Schedule, DimDate


def schedulepage(request):
    return render(request, 'firstapp/mainpage.html')


def topic(request):
    print("Got this")
    dicto = [
        {"id": "1", "name": "Java"},
        {"id": "2", "name": "C++"},
        {"id": "3", "name": "Python"},
        {"id": "4", "name": "JavaScript"}
    ]
    topiclist = json.dumps(dicto)
    return HttpResponse(topiclist)


def schedule(request):
    time = TimeTable.objects.raw(''' Select timeId, category from firstapp_TimeTable''')
    time_lst = [{"timeId": entry.timeId, "category":entry.category} for entry in time]
    #print(time_lst)
    return render(request, 'firstapp/scheduleTable.html', {'time_slot': time_lst})


def empData(request):
    empId = request.GET.get('empId', None)
    data = DimEmployee.objects.raw(''' Select * from firstapp_DimEmployee where EmpId = %s ''', [empId])
    lst = [{"id": entry.empId, "firstName":entry.firstName, "lastName":entry.lastName, "job":entry.status} for entry in data]
    send_data = json.dumps(lst)
    return HttpResponse(send_data)


def emp_schedule(request):
    empId = request.GET.get('empId', None)
    data1 = DimEmployee.objects.get(empId=empId)
    print(data1)
    data = Schedule.objects.filter(employee=data1)
    lst = [{"Id": str(d.scheduleId),
            "date_full": str(d.keyDate.FullDate),
            "shift": str(d.shift.category),
            "start_time": str(d.shift.startTime),
            "end_time": str(d.shift.endTime)}
           for d in data]

    send_data = json.dumps(lst)
    return HttpResponse(send_data)


def emp_save_data(request):
    empId = request.GET.get('empId', None)
    date = request.GET.get('date', None)
    time_slot = request.GET.get('time_slot', None)
    emp_data = DimEmployee.objects.get(empId=empId)
    date_data = DimDate.objects.get(FullDate=date)
    time_data = TimeTable.objects.get(timeId=time_slot)
    check_data = Schedule.objects.filter(employee=emp_data, keyDate=date_data, shift=time_data)
    if check_data.count() == 0:
        terms = Schedule.objects.aggregate(Max('scheduleId'))
        count = int(terms['scheduleId__max']) + 1
        print(count)
        n = Schedule(scheduleId=count, keyDate=date_data, employee=emp_data, shift=time_data)
        n.save()
        lst = ["Done"]
    else:
        lst = ["Undone"]

    return HttpResponse(json.dumps(lst))


def delete_schedule(request):
    id_list = request.GET.get('list', None);
    id_list = json.loads(id_list)
    for id in id_list:
        Schedule.objects.filter(scheduleId=id).delete()
    return HttpResponse("")