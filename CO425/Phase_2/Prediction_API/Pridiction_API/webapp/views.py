from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
import joblib
from . serialiazer import houseSerializer   

class priceCalculator(APIView):

    
    def post(self, request):
        serialiazer = houseSerializer(data=request.data)

        if serialiazer.is_valid():
            return Response(
                joblib.load('./webapp/rf_model.sav')
                .predict([[
                serialiazer.data.get('location'), 
                4,  
                2, 
                1750, 
                6.5
                ]])
                )



            