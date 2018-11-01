from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView


# Create your views here.

class Login(APIView):
    def get(self, requset):
        """

        :param requset:
        :return:
        """
        return HttpResponse('111k')
