from ast import Pass
from urllib import response
from .models import Movies
from .serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status


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
      

    
        
