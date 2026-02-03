"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from proyectos import views  # 1

urlpatterns = [
    path('admin/', admin.site.urls),  # 2
    path('', views.projects_list, name='projects_list'),  # 3
    path('project/<int:pk>/', views.project_detail, name='project_detail'),  # 4
    path('testcase/<int:pk>/', views.testcase_detail, name='testcase_detail'),  # 5

    # CRUD de ReportFile (archivos del test case)
    path('testcase/<int:pk>/reports/new/', views.report_create, name='report_create'),  # 6
    path('reports/<int:id>/edit/', views.report_edit, name='report_edit'),  # 7
    path('reports/<int:id>/delete/', views.report_delete, name='report_delete'),  # 8
]