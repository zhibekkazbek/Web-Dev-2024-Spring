from django.urls import path, re_path

from . import views
urlpatterns = [
    path('companies/', views.get_companies),
    path('companies/<int:pk>/', views.get_company),
    path('companies/<int:pk>/vacancies/', views.get_company_vacancies),
    path('vacancies/', views.get_vacancies),
    path('vacancies/<int:pk>/', views.get_vacancy),
    path('vacancies/top_ten/', views.get_top_ten),
]