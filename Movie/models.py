from tokenize import Token
from uuid import UUID
from django.db import models
import uuid
from django.core.validators import MinValueValidator , MaxValueValidator
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
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
    date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=True , blank=True)
    
    def __str__(self):
        return str(self.title)
    
    def save (self , *args, **kwargs):       
        self.slug =slugify(self.title) 
        super().save(*args,**kwargs)

    class Meta :
        ordering=['-date']
        verbose_name_plural='Movies'
    
    
@receiver(post_save , sender=User  )
def creat_token(sender ,instance,created,**kwargs):
    if created:
        Token.objects.create(user=instance)
    

# def creat_token(sender , **kwargs):
#     if kwargs['created']:
#         Token.objects.create(user=kwargs['instance'])
# post_save.connect(creat_token , sender=User)   