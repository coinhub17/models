from django.Http import HttpresponseRedirect,HttpResponse
from django.shortcut import render,redirect


if password == password2:
      if User.objects.filter(username=username).exists():
        messages.error(request, 'That username is taken')
        return redirect('accounts:register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'That email is being used')
          return redirect('accounts:register')
        else:
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
        
          user.save()
          messages.success(request, 'You are now registered and can log in')
          return redirect('Account:login')
    else:
      messages.error(request, 'Passwords dont match')
      return redirect('accounts:register')
  else:
    return render(request, 'accounts/register.html')

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are logged in')
      return HttpResponseredirect('Account:dashboard')
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('Account:login')
  else:
    return render(request, 'accounts/login.html')