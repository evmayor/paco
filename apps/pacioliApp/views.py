from django.shortcuts import render
from rest_framework import serializers, filters, viewsets, generics
from rest_framework.response import Response

from apps.pacioliApp.models import PgPlan, PgDiario,PgDiariolibro
from apps.pacioliApp.serializers import planSerializer, PlanshortSerializer, libroDiarioSerializer, libroDiarioShortSerializer
from django.db.models import Q, Max


class planViewSet(viewsets.ModelViewSet):
    queryset = PgPlan.objects.filter(nnivel=3)
    serializer_class = planSerializer

    def listaPlanes(self, repuest, *args, **kwargs):
        plan = PgPlan.objects.filter(nnivel = 3)
        serializer = PlanshortSerializer(plan, many=True)
        return Response(serializer.data)


class PurchaseList(generics.ListAPIView):
    queryset = PgPlan.objects.filter(neducat=3)
    serializer_class = planSerializer
    
    def get_queryset(self,request,format=None):
        simple = self.kwargs['neducat']
        queryset = PgPlan.objects.filter(neducat=simple)
        return queryset


class listado(viewsets.ModelViewSet):
    serializer_class = planSerializer
    def get_queryset(self, *args, **kwargs):
        serializer_class = planSerializer
        queryset = PgPlan.objects.filter(neducat=5)
        return queryset
        
        
class listadob(viewsets.ModelViewSet):
    serializer_class = planSerializer
    def get_queryset(self):
        if self.request.method == 'GET':
            queryset=PgPlan.objects.all()
            neducat= self.request.GET.get('q',None)
            if neducat is not None:
                queryset = PgPlan.objects.filter(neducat=neducat)
        return queryset


class libroDiarioViewSet(viewsets.ModelViewSet):
    queryset = PgDiariolibro.objects.all()
    serializer_class = libroDiarioSerializer

    def listaPlanes(self, repuest, *args, **kwargs):
        diario = PgDiariolibro.objects.all()
        serializer = libroDiarioShortSerializer(diario, many=True)
        return Response(serializer.data)


class asientoMaxViewSet(viewsets.ModelViewSet):
    queryset = PgDiariolibro.objects.aggregate(Max('nasiento'))
    serializer_class = libroDiarioSerializer

    def listaPlanes(self, repuest, *args, **kwargs):
        plan = PgDiariolibro.objects.aggregate(Max('nasiento'))
        serializer = libroDiarioShortSerializer(plan, many=True)
        return Response(serializer.data)