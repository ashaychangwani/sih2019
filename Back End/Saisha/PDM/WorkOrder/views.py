from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from .models import WorkOrder


def DisplayWorkOrders(request):
    wo = WorkOrder.objects.all()
    context = {
        'wo': wo,
    }
    return HttpResponse(render(request, 'workorder/wo.html', context))

def WorkOrderForm(request):
    if request.method == 'POST' :
        WorkOrderNum = request.POST.get('wo', False)
        Description = request.POST.get('des', False)
        DataStamp = request.POST.get('date', False)
        StartTime = request.POST.get('start', False)
        EndTime = request.POST.get('end', False)
        Status = request.POST.get('status', False)
        Cost = request.POST.get('cost', False)
        wo = WorkOrder(WorkOrderNum=WorkOrderNum, Description=Description, DataStamp=DataStamp, StartTime=StartTime, EndTime=EndTime, Status=Status, Cost=Cost)
        wo.save()
    return HttpResponse(render(request, 'workorder/woform.html'),{})