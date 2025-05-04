from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Pet, AnimalType
from .forms import PetForm, LoginForm


def log_in(request):
    form = LoginForm(request.POST or None)
    context = {'message': None, 'form': form}
    if request.POST and form.is_valid():
        user = authenticate(**form.cleaned_data)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('pets:home')
            else:
                context['message'] = 'El usuario ha sido desactivado'
        else:
            context['message'] = 'Usuario o contraseña incorrecta'
    return render(request, 'pets/login.html', context)


@login_required
def log_out(request):
    logout(request)
    return redirect('pets:log-in')


@login_required
def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})


@login_required
def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'pets/detail.html', {'pet': pet})


@login_required
def pet_create(request):
    form = PetForm(request.POST or None, request.FILES or None)
    if request.POST and form.is_valid():
        form.save()
        return redirect('pets:home')
    return render(request, 'pets/form.html', {'form': form})


@login_required
def pet_update(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if request.POST and form.is_valid():
        form.save()
        return redirect('pets:home')
    return render(request, 'pets/form.html', {'form': form})


@login_required
def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    pet.delete()
    return redirect('pets:home')


@login_required
def animal_type_list(request):
    types = AnimalType.objects.all()
    return render(request, 'pets/category/animal_type_list.html', {'types': types})
