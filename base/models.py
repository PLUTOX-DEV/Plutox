from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
# Create your models here.

class User(AbstractUser):
    name =models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True , null=True)
    username = models.CharField(null=True, blank=True, max_length=255)
    bio = models.TextField(null=True)
    
    avatar =models.ImageField(
        default= 'avatar.svg ' ,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'png', 'jpeg' , 'svg'])]
    )
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    
def __str__(self):
    return self.username

def __save__(self,*args,**kwargs):
    email_username,_ = self.email.split('@')
    
    if self.username == "" or self.username == None:
        self.username = email_username
        
        
        super(User, self).save(*args,**kwargs)  

    
# Create your models here.
class Topic (models.Model):
    name = models.CharField(max_length=200) 
    def __str__(self) :
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name= 'participants')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-updated','-created'] 
    
    def __str__(self) :
        return self.name

class Message (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated','-created'] 
    
    def __str__(self) :
        return self.body[0:50] 
    
    

