from django.shortcuts import render

# Create your views here.
# article/views.py


from rest_framework import generics
from peprclip.models import peprclip_function
from peprclip.serializers import Peprclip_function_serializer, Peprclip_function_detail_serializer

def function_list(ListCreateAPIView):
    queryset = peprclip_function.objects.all()
    serializer_class = Peprclip_function_serializer
    # if request.method == 'GET':
    #     functions = peprclip_function.objects.all()
    #     serializer = Peprclip_function_serializer(functions, many=True)
    #     return Response(serializer.data)

def function_detail_list(RetrieveUpdateDestroyAPIView):
    queryset = peprclip_function.objects.all()
    lookup_url_kwarg = 'id'
    serializer_class = Peprclip_function_detail_serializer

