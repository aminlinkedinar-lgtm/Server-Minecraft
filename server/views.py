from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home_server_viwe(request):
    return render(request, 'Home.html')

def server_list_viwe(request):
    server = Server.objects.filter(server_owner=request.user)
    context = {'server':server}
    return render(request, 'server_list.html', context)

def add_server_viwe(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            server = form.save(commit=False)
            server.server_owner = request.user
            server.save()
            return redirect('server_list')
    else:
        form = ServerForm() 

    context = {'form': form}
    return render(request, "add_server.html", context)        

def server_information_viwe(request):
    server_id = request.GET.get("id")
    if server_id:
        server = Server.objects.get(id=server_id, server_owner = request.user)
    else:    
        server = Server.objects.all().first()

    context = {'server_name':server.server_name,
                'version':server.version,
                'ip':server.ip,
                'description':server.description,
                'number_of_players': server.number_of_players,
                'server_status':server.server_status,
                'creation_data':server.creation_data,
                'server_owner':server.server_owner,    
                }

    return render(request, "show_server_information.html", context)

def delete_server_viwe(request):
    if request.method == "POST":
        server_id = request.POST.get('id')
        server = Server.objects.filter(id=server_id, server_owner = request.user).filter()
        if server:
            server.delete()
    return redirect('server_list')

def update_server_viwe(request, id):
    server = Server.objects.get(id=id, server_owner = request.user)

    if request.method == "POST":
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            return redirect('server_list')
    else:
        form = ServerForm(instance=server)

    context = {'form':form}   
    return render(request, "update_server.html", context)

def register_server_viwe(request):
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('home')
    else:
        form = UserCreationForm()
        
    context = {'form':form}
    return render(request, "register.html", context)        

def profile_server_viwe(request):
    profile_id = request.GET.get("id")
    if profile_id:
        profile = Profile.objects.get(id=profile_id)
    else:    
        profile = Profile.objects.get(user=request.user)
        if profile is None:
            return render(request, 'profile.html', {"massage":"dont ther"})
    
    context = {'user':profile.user,
                'first_name':profile.first_name,
                'last_name':profile.last_name,
                'phone_number':profile.phone_number,
                'biography':profile.biography,
                'date_of_birth':profile.date_of_birth,
                'city':profile.city,    
                }

    return render(request, "Profile.html", context)

@login_required
def create_profile_viwe(request):
    if  request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = ProfileForm()

        context = {'form': form}
        return render(request, "add_profile.html", context)    

@login_required
def edit_profile_viwe(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'form':form}   
    return render(request, "edit_profile.html", context)

def delete_account_view(request):
    if request.method == "POST":
            request.user.delete()
            return redirect('home')
    
    return render(request, "delete_account.html")































