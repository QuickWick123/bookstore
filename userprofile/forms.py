from django.contrib.auth.forms import UserCreationForm
 
class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ('username', 'password1', 'password2', )