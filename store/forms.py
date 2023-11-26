from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from django import forms


from .models import Order


class OrderForm(ModelForm):
<<<<<<< HEAD
    class Meta:
        model = Order
        fields = '__all__'

=======
	class Meta:
		model = Order
		fields = '__all__'
>>>>>>> 83eefd59f67ee10e99ca622bfd74c06a306dd4ee

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
