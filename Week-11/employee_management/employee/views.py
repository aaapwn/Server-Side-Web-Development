from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from employee.models import *
from company.models import *
from .forms import EmployeeForm, ProjectFrom
from django.db import transaction
# Create your views here.

class Index(View):
    def get(self, request):
        return redirect("employee-list")

class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all().order_by("-hire_date")
        for employee in employees:
            employee.position = Position.objects.get(pk=employee.position_id)
        return render(request, "employee.html", {"employees": employees})

class EmployeeRegister(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, "employee_form.html", {"form": form})

    @transaction.atomic
    def post(self, request):
        form = EmployeeForm(request.POST)
        # print(form)
        if form.is_valid():
            new_emp = form.save()
            new_emp.position_id = form.cleaned_data.get("position").id
            new_emp.save()
            EmployeeAddress.objects.create(
                employee=new_emp,
                location=form.cleaned_data.get("location"),
                district=form.cleaned_data.get("district"),
                province=form.cleaned_data.get("province"),
                postal_code=form.cleaned_data.get("postal_code")
            )
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
            return render(request, "project_detail.html", {"form": form, "id": pk})

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
