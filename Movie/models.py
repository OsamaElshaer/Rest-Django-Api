from pyexpat import model
from tabnanny import verbose
from turtle import title
from uuid import UUID
from django.db import models
import uuid
from django.core.validators import MinValueValidator , MaxValueValidator
# Create your models here.
geners=[
    ('Action','Action'),
    ('Comedy','Comedy'),
    ('Drama','Drama'),
    ('Fantasy','Fantasy'),
    ('Horror','Horror'),
    ('Mystery','Mystery'),
    ('Romance','Romance'),
    ('Thriller','Thriller'),
    ('Western' , 'Western')
]
quality=[
    ('HD','HD'),
    ('CAM','CAM'),
]

class Movies(models.Model):
    uuid=models.UUIDField(default=uuid.uuid4 ,primary_key=True )
    title=models.CharField(max_length=50 , null=True , blank=True)
    gener=models.CharField(max_length=10 ,choices=geners  , null=True , blank=True)
    rate=models.IntegerField(validators=[MaxValueValidator(10),MinValueValidator(1)] ,null=True , blank=True)
    quality=models.CharField(max_length=5,choices=quality,null=True,blank=True)
    
    def __str__(self):
        return self.title

    class Meta :
        verbose_name_plural='Movies'