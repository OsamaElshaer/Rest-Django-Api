from .models import *
from rest_framework import routers, serializers, viewsets




class MovieSerializer(serializers.ModelSerializer):
    class Meta :
        model = Movies
        fields=['uuid','title','gener','rate' , 'quality']