from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app_random_number.service import random_num
import requests
import time

class Number(APIView):
    def get(self, request):
        int_num = random_num()
        json_anwser = {"number": int_num}
        return Response(json_anwser)


class TimeCount(APIView):
    def get(self, request):
        start_time = time.time()
        response = requests.get("http://127.0.0.1:3333/")
        end_time = time.time()
        response_time_ms = (end_time - start_time) * 1000
        print(f"Время ответа: {response_time_ms:.2f} мс")

