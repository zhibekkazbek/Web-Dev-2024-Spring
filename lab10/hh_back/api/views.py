import json
from django.http import JsonResponse, Http404
from django.shortcuts import get_object_or_404
from api.models import Company, Vacancy
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from api.serializers import CompanySerializer, VacancySerializer

# Create your function based views / FBV here.
@csrf_exempt
def get_companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        # companies_json = [c.to_json() for c in companies ]
        serializer = CompanySerializer(companies, many=True)
        # return JsonResponse(companies_json, safe=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(name=data.get("name"))
        return JsonResponse(company.to_json())

@csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def get_company(request, pk=None):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400)

    if request.method == 'GET':
        # return JsonResponse(company.to_json())
        serializer = CompanySerializer(company, many=True)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data.get("name")
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({"deleted": True})

def get_company_vacancies(request, pk=None):
    try:
        company = Company.objects.get(id=pk)
    except Company.DoesNotExist as e:
        return JsonResponse({"error": str(e)}, status=400)

    vacancies_json = [v.to_json() for v in company.vacancies.all()]

    return JsonResponse(vacancies_json, safe=False)


# Class based views for Vacanies

class VacancyList(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = VacancySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class VacancyDetail(APIView):
    def get_object(self,id):
        try:
            return Vacancy.objects.get(pk=id)
        except Vacancy.DoesNotExist:
            raise Http404
    
    def get(self,request,pk):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)
    

    def put(self,request,pk):
        vacancy = self.get_object(pk)
        serializer = VacancySerializer(vacancy,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response({"deleted": True},status=status.HTTP_204_NO_CONTENT)
    
def get_top_ten(request, pk=None):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    # vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)