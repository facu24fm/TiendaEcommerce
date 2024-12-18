from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .formulario import RegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Vista para el registro
def registro(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda y encripta automáticamente
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'usuarios/register.html', {'form': form})


# Vista para el login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

        else:
            messages.error(request, 'Formulario inválido.')
            
    else:
        form = LoginForm()

    return render(request, 'usuarios/login.html', {'form': form})



@login_required
def home(request):
    return render(request, 'home.html')

from django.contrib.auth import logout

