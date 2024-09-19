from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("employee", views.EmployeeView.as_view(), name="employee-list"),
    path("employee/register", views.EmployeeRegister.as_view(), name="employee-register"),
    path("position", views.PositionListView.as_view(), name="position-list"),
    path("project", views.ProjectListView.as_view(), name="project-list"),
    path("project/<int:pk>", views.ProjectEditView.as_view(), name="project-edit"),
    path("project/register", views.ProjectRegister.as_view(), name="project-register"),
    path("staff/proj/<int:proj_id>/emp/<int:emp_id>", views.ManageStaff.as_view(), name="manage-staff"),
]
