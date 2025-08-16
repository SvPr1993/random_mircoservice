from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app_random_number.service import random_num


class Number(APIView):
    def get(self, request):
        int_num = random_num()
        json_anwser = {"number": int_num}
        return Response(json_anwser)
