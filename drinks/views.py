from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drinks import serializers

# views are created to see the endpoints. endpoints are a certain url that you can access data from

# A decorator gets put above a function to describe the function below it
@api_view(['GET','POST'])
def drink_list(request,format = None):

    if request.method == 'GET':
        # Gets all the drinks
        # set to variable
        drinks = Drink.objects.all()
        # set to variable
        #This serializes all of the drinks within the drink list
        serializer = DrinkSerializer(drinks, many=True)
        # put the Json response in a dictionary to separate the sodas / objects into two separate objects (shown in Json format)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# SEt decorator
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format = None):
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response  (status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': # Shows Data / Grabs data from database
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT': # Updates Data
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE': 
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
