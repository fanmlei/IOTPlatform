from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from website import database

# Create your views here.

class Login(APIView):
    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res = database.login(username, password)
        return JsonResponse(res)

class Register(APIView):
    def post(self,request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res = database.register(username,password)
        return JsonResponse(res)