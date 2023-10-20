from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects),
    path('project/<str:teamId>/', views.projectDetails),
    # path('projects/year/<int:year>/', views.ssrYear),
    # path('projects/category/<str:category>/', views.ssrCategory),
    # path('projects/year/', views.getYears),
    # path('projects/category/', views.getCatories),
    # path('projects/teams/', views.teams),
]