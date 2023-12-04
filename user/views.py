from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

from .models import Profile
from django.contrib.auth.models import User, Group
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, AdminUpdateForm
#from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail

# Create your views here.

def register(request):
    # Extraer formulario de Usurio de la Vista (POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        # username y pswd validos [CSRF]
        if form.is_valid(): 
            user = form.save() 
            group = Group.objects.get(name='accountant')
            user.groups.add(group)

            messages.success( request, 'Usuario registrado exitosamente.')

            # Enviar correo de bienvenida
            send_mail(
                'Welcome to Oil Stock Manager!',

                f'Hola {user.username}!'+
                "\n\nGracias por registrarse con nosotros. Apreciamos su interés en este proyecto." +
                "\nNuestra intención es brindarle el mejor servicio posible, así que no dude en contactarnos." +
                "\nSin nada más que decir, disfruta de nuestra Aplicación y no dudes en recomendarnos (y quiza hacer una donación :D)" +
                "\n\nTe deseamos todo lo mejor." +
                "\nProyecto de Bases :3"
                ,

                'oilstockmanager@gmail.com',
                [user.email],
                fail_silently=False,
            )

            return redirect('login')
        
        else:
            if 'username' in form.errors:
                messages.warning( request, 'Este usuario ya esta registrado.')

            elif 'password1' in form.errors and not 'password2' in form.errors:
                messages.error( request, 'Contraseña invalida.')

            else:
                messages.error( request, 'Contraseña insegura o Confirmacion invalida.')

            return redirect('register')

    # Acceder a la pagina de register mediante hipervinculos
    else: form = CreateUserForm()

    context = { 'form' : form }
    return render(request, 'register.html', context)


@login_required
def custom_logout(request): 

    logout(request)
    messages.info(request, 'Ha cerrado sesion satisfactoriamente.')
    
    return redirect('login')

@login_required
def profile(request):
    return render( request, 'profile.html' )

@login_required
def profile_update(request):
    # instance = request.user -> polula automaticamente el formulario con la informacion original
    if request.method == 'POST':
        user_form = UserUpdateForm( request.POST, instance = request.user )
        profile_form = ProfileUpdateForm( request.POST, request.FILES, instance = request.user.profile )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(); profile_form.save()
            return redirect( 'profile' )

    else:
        user_form = UserUpdateForm( instance = request.user )
        profile_form = ProfileUpdateForm( instance = request.user.profile )


    context = { 'user_form' : user_form, 'profile_form' : profile_form }
    return render( request, 'profile_update.html', context)



# USERS ADMINISTRATION
@login_required
def staff(request): 
    staff_list = User.objects.all()
    
    context = { 'staff_list' : staff_list }
    return render(request, 'staff.html', context)

@login_required
def staff_detail(request, pk):
    current_staff = User.objects.get(id = pk)
    current_profile = Profile.objects.get( profile = current_staff )

    if request.method == 'POST':
        form = AdminUpdateForm( request.POST, instance = current_profile )

        if form.is_valid():
            form.save()
            return redirect('staff_detail', pk = pk )
        
    else:
        form = AdminUpdateForm( instance = current_profile )
    
    context = { 'staff': current_staff, 'form' : form }
    return render(request, 'staff_detail.html', context)

@login_required
def staff_delete(request, pk):
    current_staff = User.objects.get(id = pk)

    if request.method == 'POST':
        current_staff.delete()
        return redirect('staff')
    
    context = { 'staff': current_staff }
    return render(request, 'staff_delete.html', context)

@login_required
def staff_active(request, pk):
    current_staff = User.objects.get(id = pk)

    if request.method == 'POST':
        current_staff.is_active = True
        current_staff.is_staff = False
        current_staff.is_superuser = False

        current_staff.save()
        return redirect('staff_detail', pk = pk )
    
    context = { 'staff': current_staff }
    return render(request, 'staff_active.html', context)
@login_required
def staff_staff(request, pk):
    current_staff = User.objects.get(id = pk)

    if request.method == 'POST':
        current_staff.is_active = True
        current_staff.is_staff = True
        current_staff.is_superuser = False

        current_staff.save()
        return redirect('staff_detail', pk = pk )
    
    context = { 'staff': current_staff }
    return render(request, 'staff_staff.html', context)
@login_required
def staff_super(request, pk):
    current_staff = User.objects.get(id = pk)

    if request.method == 'POST':
        current_staff.is_active = True
        current_staff.is_staff = True
        current_staff.is_superuser = True

        # current_group = current_staff.groups.values_list('name', flat=True)[0]
        # current_group = Group.objects.get(name = current_group)
        # current_staff.groups.remove(current_group)

        # new_group = Group.objects.get(name = 'manager')
        # current_staff.groups.remove(new_group)

        current_staff.save()
        return redirect('staff_detail', pk = pk )
    
    context = { 'staff': current_staff }
    return render(request, 'staff_super.html', context)