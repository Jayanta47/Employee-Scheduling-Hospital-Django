from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from firstapp.models import DimEmployee


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
    data = DimEmployee.objects.raw(''' Select * from firstapp_DimEmployee where Status = 'Doctor' ''')
    lst = [{"id": entry.empId, "firstName":entry.firstName, "lastName":entry.lastName, "job":entry.status} for entry in data]
    print(lst)
    return render(request, 'firstapp/scheduleTable.html')


def empData(request):
    empId = request.GET.get('empId', None)
    print(empId)
    data = DimEmployee.objects.raw(''' Select * from firstapp_DimEmployee where EmpId = %s ''', [empId])
    lst = [{"id": entry.empId, "firstName":entry.firstName, "lastName":entry.lastName, "job":entry.status} for entry in data]
    print(lst)
    send_data = json.dumps(lst)
    return HttpResponse(send_data)
