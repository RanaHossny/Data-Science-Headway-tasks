from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import KPI, AssetKPI
from .serializers import KPISerializer, AssetKPISerializer
from drf_yasg.utils import swagger_auto_schema
from .sw.my_software.Software_Ingestor.Data_Ingestor_Proxy import Ingestor_Proxy
import pandas as pd
import os
import json

data_path = os.path.join(os.getcwd(), "kpi\example.txt")
with open(data_path, 'r') as file:
    data = [json.loads(line) for line in file]
df_data=pd.DataFrame(data)

# #if want to run as example one uncomment this
# equation_path=os.path.join(os.getcwd(), "kpi\Equation.txt")
# processing_engine_args=['Text',equation_path,False]
# ingertor_args=["Json",data]

# data_sink_args=['Mysql','localhost','assets_db','root','Rana@1234']
# # data_sink_args=['Raw'] # datasink
# my_data_ingestor=Ingestor_Proxy(ingertor_args,processing_engine_args,data_sink_args)
# my_data_ingestor.send_msg()


@swagger_auto_schema(method='post', request_body=KPISerializer)
@api_view(['GET', 'POST', 'DELETE'])

def kpi_list_create(request):
    if request.method == 'GET':
        kpis = KPI.objects.all()
        serializer = KPISerializer(kpis, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KPISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kpi_id = request.data.get('id')
        try:
            kpi = KPI.objects.get(id=kpi_id)
            kpi.delete()
            return Response({"message": "KPI deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except KPI.DoesNotExist:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='post', request_body=AssetKPISerializer)  
@api_view(['POST'])
def link_asset_to_kpi(request):
    if request.method == 'POST':
        with open(data_path, 'r') as file:
            data = [json.loads(line) for line in file]
        df_data=pd.DataFrame(data)
        serializer = AssetKPISerializer(data=request.data)
        asset_id = request.data.get("asset_id")   
        # Check if asset_id exists in the DataFrame
        if asset_id not in df_data["asset_id"].values:
            return Response({"error": "Asset ID not found"}, status=status.HTTP_400_BAD_REQUEST)
        kpi = KPI.objects.filter(id=request.data.get("kpi")).first() 
        kpi_data = KPISerializer(kpi).data 
        filtered_data = df_data[df_data['asset_id'] == asset_id]
        processing_engine_args=['Json',[kpi_data['expression']]]
        ingertor_args=['Json',[filtered_data]]
        data_sink_args=['Raw'] # datasink
        my_data_ingestor=Ingestor_Proxy(ingertor_args,processing_engine_args,data_sink_args)
        my_data_ingestor.send_msg()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


