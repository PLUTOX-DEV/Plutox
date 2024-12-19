 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from     .models import Room , User


class MyUsercreationform(UserCreationForm):
    class Meta:
        model = User
        fields = ( 'name', 'username', 'email', 'password1', 'password2')

class RoomFroms(ModelForm):
    class Meta:
        model = Room 
        fields = '__all__'
        exclude = ['host', 'participants' ]
  
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'name', 'email' , 'bio' ]  


