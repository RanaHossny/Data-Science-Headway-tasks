from django.shortcuts import render
import uuid

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import KPI, AssetKPI,AssetAttribute,Simulator
from .serializers import KPISerializer, AssetKPISerializer,SimulatorSerializer,AssetAttributeSerializer
from drf_yasg.utils import swagger_auto_schema
from .sw.my_software.Software_Ingestor.Data_Ingestor_Proxy import Ingestor_Proxy
import pandas as pd
import os
import json


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
@api_view(['GET','POST'])
def link_asset_to_kpi(request):
    if request.method == 'GET':
        kpis_asset = AssetKPI.objects.all()
        serializer = AssetKPISerializer(kpis_asset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        asset_id = request.data.get("asset_id") or str(uuid.uuid4())
        serializer = AssetKPISerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        kpi = KPI.objects.filter(id=request.data.get("kpi")).first() 
        kpi_data = KPISerializer(kpi).data 
        filtered_data = {"value": request.data.get("asset_value"),
                         "attribute_id":asset_id}
        processing_engine_args=['Json',[kpi_data['expression']]]
        ingertor_args=['Json',[filtered_data]]
        data_sink_args=['Raw'] # datasink
        my_data_ingestor=Ingestor_Proxy(ingertor_args,processing_engine_args,data_sink_args)
        my_data_ingestor.send_msg()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@swagger_auto_schema(method='post', request_body=AssetAttributeSerializer)
@api_view(['GET', 'POST'])
def Attribute_veiw(request):
    if request.method == 'GET':
        asset_attributes = AssetAttribute.objects.all()
        serializer = AssetAttributeSerializer(asset_attributes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AssetAttributeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='post', request_body=SimulatorSerializer)
@api_view(['GET', 'POST'])
def Simulator_veiw(request):
    if request.method == 'GET':
        simulators = Simulator.objects.all()
        serializer = SimulatorSerializer(simulators, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SimulatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)