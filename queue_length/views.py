from django.shortcuts import render

# Create your views here.
from .models import Logdata_put
from .serializers import Logdata_putSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

@api_view(['GET'])
def queue_length(request):
	queue=Logdata_put.objects.first()
	queue_serializer=Logdata_putSerializer(queue,many=False)
	return JsonResponse(queue_serializer.data)


@api_view(['PUT'])
def queue_length_update(request):
	log_put=Logdata_put(queue_length=request.data['queue_length'])
	log_put.save();
	queue=Logdata_put.objects.first()
	queue_serializer=Logdata_putSerializer(queue,data=request.data)
	if queue_serializer.is_valid():
		queue_serializer.save()
		return JsonResponse(queue_serializer.data, status=status.HTTP_201_CREATED)
	return JsonResponse(queue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_updates(request):
	allupdates=Logdata_put.objects.all()
	queue_serializer=Logdata_putSerializer(allupdates,many=True)
	return JsonResponse(queue_serializer.data, safe=False)