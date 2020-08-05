from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        print(username, password, password2)

        user = User()
        user.username = username
        user.set_password(password)
        user.save()
        return render(request, 'accounts/signup_complete.html')
    else:
        context_values = {'form': 'this is form'}
        return render(request, 'accounts/signup.html', context_values)
