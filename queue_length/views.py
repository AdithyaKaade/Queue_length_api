from django.shortcuts import render
from datetime import datetime, timezone, timedelta
# Create your views here.
from .models import Logdata_put
from .serializers import Logdata_putSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
import time
import math

@api_view(['GET'])
def queue_length(request):
	queue=Logdata_put.objects.last()
	queue_serializer=Logdata_putSerializer(queue,many=False)
	return JsonResponse(queue_serializer.data)


@api_view(['POST'])
def queue_length_update(request):
	time_threshold = datetime.now(timezone.utc) - timedelta(minutes=5)
	queue=Logdata_put.objects.filter(updated_time__gte=time_threshold)
	max_len = -math.inf
	for items in queue:
		max_len = max(max_len, items.queue_length)	
	#load the data into the dataset
	log_put=Logdata_put(queue_length=request.data['queue_length'])

	if(max_len - int(log_put.queue_length) >= 50 ):
		return JsonResponse({"Invalid" : "queue_length"})

	queue_serializer=Logdata_putSerializer(data=request.data)
	if queue_serializer.is_valid():
		# saves the updates value
		queue_serializer.save()
		return JsonResponse(queue_serializer.data, status=status.HTTP_201_CREATED)
	return JsonResponse(queue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_updates(request):
	allupdates=Logdata_put.objects.all()
	queue_serializer=Logdata_putSerializer(allupdates,many=True)
	return JsonResponse(queue_serializer.data, safe=False)