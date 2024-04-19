from . import views
from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("admin-dashboard", views.admin_dashboard, name ="adminDashboard")
]
