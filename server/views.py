from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

def home_server_viwe(request):
    return render(request, 'Home.html')

@login_required
def server_list_viwe(request):
    search = request.GET.get("search")
    sort = request.GET.get("sort")
    server = Server.objects.filter(server_owner=request.user)
    if search:
        server = server.filter(server_name__icontains=search)
        
    if sort == "newest":
        server = server.order_by("-creation_data")

    elif sort == "oldest":
        server = server.order_by("creation_data")

    elif sort == "players":
        server = server.order_by("-number_of_players")

    elif sort == "low_players":
        server = server.order_by("number_of_players")

    elif sort == "online":
        server = server.filter(server_status=True)

    elif sort == "offline":
        server = server.filter(server_status=False)            
    
    paginator = Paginator(server, 5)
    page_number = request.GET.get("page")
    server = paginator.get_page(page_number)
    
    context = {'server':server}
    return render(request, 'server_list.html', context)

@login_required
def add_server_viwe(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            server = form.save(commit=False)
            server.server_owner = request.user
            server.save()
            messages.success(request, "Server delete successfully")
            return redirect('server_list')
    else:
        form = ServerForm() 

    context = {'form': form}
    return render(request, "add_server.html", context)        

def server_information_viwe(request):
    server_id = request.GET.get("id")
    server = get_object_or_404(Server, id = server_id, server_owner = request.user)

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

@login_required
def delete_server_viwe(request):
    if request.method == "POST":
        server_id = request.POST.get('id')
        server = get_object_or_404(Server ,id=server_id, server_owner = request.user)

    server.delete()
    messages.success(request, "Server delete successfully.")
    return redirect('server_list')

@login_required
def update_server_viwe(request, id):
    server = get_object_or_404(Server , id=id, server_owner = request.user)

    if request.method == "POST":
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            messages.success(request, "Server update successfully.")
            return redirect('server_list')
    else:
        form = ServerForm(instance=server)

    context = {'form':form}   
    return render(request, "update_server.html", context)

def register_server_viwe(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            message.success(request, "Your account  has been created successfully.")
            return redirect('home')
    else:
        form = UserCreationForm()
        
    context = {'form':form}
    return render(request, "register.html", context)        

@login_required
def profile_server_viwe(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    context = {'user':profile.user,
                'first_name':profile.first_name,
                'last_name':profile.last_name,
                'phone_number':profile.phone_number,
                'biography':profile.biography,
                'date_of_birth':profile.date_of_birth,
                'city':profile.city,    
                }

    return render(request, "Profile.html", context)


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
    profile = get_object_or_404(Profile ,user = request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile update successfuly.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {'form':form}   
    return render(request, "edit_profile.html", context)

@login_required
def delete_account_view(request):
    if request.method == "POST":
            request.user.delete()
            messages.success(request, "Your account has been deleted.")
            return redirect('home')
    
    return render(request, "delete_account.html")































