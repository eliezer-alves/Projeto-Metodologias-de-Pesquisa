from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet


def login_user(request):
    data = {}
    data['title'] = 'Login'

    return render(request, 'login.html', data)

def logout_user(request):
    logout(request)
    return redirect('/login/')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválidos!')

    return redirect('/login/')

def index(request):
    data = {}
    data['title'] = 'Home'
    data['home'] = True;
    return render(request, 'index.html', data)

def list_all_pets(request):
    data={}
    data['title'] = 'Todos Anúncios'
    data['todos'] = True;
    pets = Pet.objects.filter(active=True)
    data['pets'] = pets

    return render(request, 'list.html', data)

@login_required(login_url='/login/')
def list_user_pets(request):
    data={}
    data['title'] = 'Meus Anúncios'
    data['meus'] = True;
    pets = Pet.objects.filter(active=True, user=request.user)
    data['pets'] = pets

    return render(request, 'list.html', data)

def pet_detail(request, id):
    data={}
    pet = Pet.objects.get(active=True, id=id)
    data['pet'] = pet
    data['meu_pet'] = False
    if request.user==pet.user:
        data['meu_pet'] = True

    return render(request, 'pet_detail.html', data)

@login_required(login_url='/login/')
def pet_register(request):
    data = {}
    data['title'] = 'Novo Anúncio'
    pet_id = request.GET.get('id')
    if pet_id:
        pet = Pet.objects.get(id=pet_id)
        return render(request, 'pet_register.html', {'pet':pet})

    return render(request, 'pet_register.html', data)

@login_required(login_url='/login/')
def set_pet(request):
    id = request.POST.get('pet_id')
    city = request.POST.get('city')
    bedrooms = request.POST.get('bedrooms')
    toilets = request.POST.get('toilets')
    peoples = request.POST.get('peoples')
    price = request.POST.get('price')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    photo = request.FILES.get('photo')
    description = request.POST.get('description')
    user = request.user
    if id:
        pet = Pet.objects.get(id=id)
        if user==pet.user:
            pet.email = email
            pet.city = city
            pet.bedrooms = bedrooms
            pet.toilets = toilets
            pet.peoples = peoples
            pet.price = price
            pet.phone = phone
            pet.description = description
            if photo:
                pet.photo = photo
            pet.save()
        #pet = Pet.objects.update(city=city, email=email, phone=phone, photo=photo, description=description, user=user)
    else:
        pet = Pet.objects.create(city=city,bedrooms=bedrooms,toilets=toilets,peoples=peoples,price=price,email=email,phone=phone,photo=photo,description=description,user=user)
    url = '/pet/detail/{}/'.format(pet.id)
    return redirect(url)

@login_required(login_url='/login/')
def pet_delete(request, id):
    pet = Pet.objects.get(id=id)
    if request.user==pet.user:
        pet.delete()
    else:
        return redirect('/login/')

    return redirect('/pet/user/')