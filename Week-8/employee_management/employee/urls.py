from django.urls import path
from . import views

urlpatterns = [
    path("", views.EmployeeListView.as_view(), name="employee-list"),
    path("position", views.PositionListView.as_view(), name="position-list"),
    path("project", views.ProjectListView.as_view(), name="project-list"),
    path("project/<int:pk>", views.ProjectEditView.as_view(), name="project-edit"),
    path("staff/proj/<int:proj_id>/emp/<int:emp_id>", views.ManageStaff.as_view(), name="manage-staff"),
]
