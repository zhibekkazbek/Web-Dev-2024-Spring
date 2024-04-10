from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Company, Vacancy
from django.shortcuts import get_object_or_404

# Create your views here.

def get_companies(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies ]
    return JsonResponse(companies_json, safe=False)

def get_company(request, pk=None):
    try:
        company = Company.objects.get(id=pk)
        return JsonResponse(company.to_json())
    except Company.DoesNotExist as e:
        return JsonResponse({
            'Error': str(e)
        })
    
def get_company_vacancies(request, pk=None):
    company = Company.objects.get(id=pk)
    vacancies = Vacancy.objects.filter(company=company.name)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [v.to_json() for v in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def get_vacancy(request, pk = None):
    try:
        vacancy = Vacancy.objects.get(id=pk)
        return JsonResponse(vacancy.to_json())
    except Vacancy.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        })
    
def get_top_ten(request, pk=None):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)