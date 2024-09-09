from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
from .forms import EmployeeForm, ProjectFrom
# Create your views here.

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all().order_by("-hire_date")
        return render(request, "employee.html", {"employees": employees})
    
class EmployeeRegister(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, "employee_form.html", {"form": form})
    
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employee-list")
        else:
            return render(request, "employee_form.html", {"form": form})

class PositionListView(View):
    def get(self, request):
        positions = Position.objects.all()
        return render(request, "position.html", {"positions": positions})

class ProjectListView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "project.html", {"projects": projects})
    
class ProjectRegister(View):
    def get(self, request):
        form = ProjectFrom()
        return render(request, "project_form.html", {"form": form})
    
    def post(self, request):
        form = ProjectFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project-list")
        else:
            return render(request, "project_form.html", {"form": form})

class ProjectEditView(View):
    def get(self, request, pk):
        project = Project.objects.get(pk=pk)
        form = ProjectFrom(instance=project)
        return render(request, "project_detail.html", {"form": form, 'id': pk, 'project': project})
    
    def post(self, request, pk):
        project = Project.objects.get(pk=pk)
        form = ProjectFrom(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project-edit", pk)
        else:
            return render(request, "project_detail.html", {"form": form})

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
    
    def get(self, request, proj_id, emp_id):
        project = Project.objects.get(pk=proj_id)
        try:
            employee = Employee.objects.get(pk=emp_id)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})
        project.staff.remove(employee)
        return redirect("project-edit", proj_id)
