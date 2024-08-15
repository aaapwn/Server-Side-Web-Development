from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class EmployeeListView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, "employee.html", {"employees": employees})

class PositionListView(View):
    def get(self, request):
        positions = Position.objects.all()
        return render(request, "position.html", {"positions": positions})

class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "project.html", {"projects": projects})

class ProjectEditView(View):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        context = {
            "project": project,
            "start_date": project.start_date.strftime("%Y-%m-%d"),
            "due_date": project.due_date.strftime("%Y-%m-%d"),
        }
        return render(request, "project_detail.html", context)

    def delete(self, request, pk):
        project = Project.objects.get(pk=pk)
        project.delete()
        return JsonResponse({"status": "ok"})

class ManageStaff(View):
    def put(self, request, proj_id, emp_id):
        project = Project.objects.get(pk=proj_id)
        try:
            employee = Employee.objects.get(pk=emp_id)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        project.staff.add(employee)
        return JsonResponse({"status": "ok"})
    
    def delete(self, request, proj_id, emp_id):
        project = Project.objects.get(pk=proj_id)
        try:
            employee = Employee.objects.get(pk=emp_id)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        project.staff.remove(employee)
        return JsonResponse({"status": "ok"})
