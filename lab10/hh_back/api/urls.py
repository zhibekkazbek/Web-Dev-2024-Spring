from django.urls import path, re_path

from api.views import VacancyList, VacancyDetail, get_companies, get_company, get_company_vacancies, get_top_ten
urlpatterns = [
    path('companies/', get_companies),
    path('companies/<int:pk>/', get_company),
    path('companies/<int:pk>/vacancies/', get_company_vacancies),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetail.as_view()),
    path('vacancies/top_ten/', get_top_ten),
]