from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, CompanyDetailSerializer
from api.serializers import VacancySerializer, VacancyDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins



class CompanyView(APIView):
    def get(self, request, format=None):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializer = CompanyDetailSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VacancyView(APIView):
    def get(self, request, format=None):
        vacancy = Vacancy.objects.all()
        serializer = VacancySerializer(vacancy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VacancyDetailView(APIView):
    def get_object(self, pk):
        try:
            return Vacancy.objects.get(pk=pk)
        except Vacancy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vacancy = self.get_object(pk)
        serializer = VacancyDetailSerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vacancy = self.get_object(pk)
        serializer = VacancyDetailSerializer(vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vacancy = self.get_object(pk)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class VacancyByCompanyView(APIView):
    def get(self, request, pk, format=None):
        vacancy = Vacancy.objects.filter(company=pk)
        serializer = VacancySerializer(vacancy, many=True)
        return Response(serializer.data)

# class VacancybycompanyAPIView(mixins.CreateModelMixin,mixins.ListModelMixin,generics.GenericAPIView):
#     def get_company(self, id):
#         try:
#             return Company.objects.get(id=id)
#         except Company.DoesNotExist as e:
#             return Response({'error': str(e)})
#     def get_vacancy(self,id):
#         return Vacancy(company = self.get_company(id))
#     def get(self,request,id,*args, **kwargs):
#         return self.list(self,request,id,*args, **kwargs)
#     def post(self,request,id,*args, **kwargs):
#         return self.create(self,request,id,*args, **kwargs)
############################################################################################
# class Vacancy_by_Company(APIView):
#     def get_object(self, id):
#         try:
#             return Company.objects.get(id=id)
#         except Company.DoesNotExist as e:
#             return Response({'error': str(e)})
#
#     def post(self, request, id):
#         vacancy = Vacancy(company = self.get_object(id))
#         serializer = VacancySerializer(vacancy, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return Response(serializer.errors)
#
#     def get(self, request, id):
#         vacancies = Vacancy.objects.filter(company = self.get_object(id))
#         serializer = VacancySerializer(vacancies, many = True)
#         return Response(serializer.data)
    # if request.method == 'GET':
    #     vacancies = Vacancy.objects.filter(company=pk)
    #     serializer = VacancyDetailSerializer(vacancies, many=True)
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = VacancyDetailSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# def company_list(request):
#     companies = Company.objects.all()
#     companies_json = [company.to_json() for company in companies]
#     return JsonResponse(companies_json, safe=False)
#
#
# def company_detail(request, company_id):
#     try:
#         company = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': 'company doesn`t exist'})
#     return JsonResponse(company.to_json())


# def vacancy_from_company(request, company_id):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = []
#     for vacancy in vacancies:
#         a = vacancy.to_json()
#         if a['company_id'] == company_id:
#             vacancies_json.append(a)
#
#     if(len(vacancies_json)):
#         return JsonResponse(vacancies_json,safe=False)
#     else:
#         return JsonResponse("Error nothing found")
#
#
#
# def vacancy_list(request):
#     vacancies = Vacancy.objects.all()
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json, safe=False)
#
#
# def vacancy_detail(request, vacancy_id):
#     try:
#         vacancy = Vacancy.objects.get(id=vacancy_id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': 'Vacancy doesn`t exist'})
#     return JsonResponse(vacancy.to_json())
#
# def vacancy_list10(request):
#     vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
#     vacancies_json = [vacancy.to_json() for vacancy in vacancies]
#     return JsonResponse(vacancies_json, safe=False)

# Create your views here.
