from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import joblib
from . serialiazer import houseSerializer   

# class priceCalculator(APIView):

    
#     def post(self, request):
#         serialiazer = houseSerializer(data=request.data)

#         if serialiazer.is_valid():
#             print(request.data)
#             return Response(
                # joblib.load('./webapp/rf_model.sav')
                # .predict([[
                # serialiazer.data.get('location'), 
                # 4,  
                # 2, 
                # 1750, 
                # 6.5
                # ]])
#                 )

def home(request):
    print(request.GET.get('location'))
    return HttpResponse(joblib.load('./webapp/rf_model.sav')
                .predict([[
                request.GET.get('location'), 
                request.GET.get('beds'),  
                request.GET.get('baths'), 
                request.GET.get('house_size'), 
                request.GET.get('land_size')
                ]]))

            