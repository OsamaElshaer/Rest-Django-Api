from ast import Pass
from urllib import response
from .models import Movies
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# FBV Function based views 
# GET POST

@api_view(['GET','POST'])
def fbvlistapi(request):
    #GET
    if request.method=='GET':
        movies=Movies.objects.all()
        serializer=MovieSerializer(movies , many=True)
        return Response (serializer.data)
    #POST

    elif request.method == 'POST':
        serializer = MovieSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def fbvslugapi(request,slug):
    try:
        movie=Movies.objects.get(slug=slug)
    except Movies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method=='GET':
        serializer=MovieSerializer(movie)
        return Response (serializer.data)

    #PUT
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    #DELETE
    if request.method=='DELETE':
        movie.delete()
        return Response (status= status.HTTP_204_NO_CONTENT)
    
