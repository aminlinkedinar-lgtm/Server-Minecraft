from django.shortcuts import render,redirect
from .models import Server
import requests
from .forms import ServerForm
# Create your views here.

def home_server_viwe(request):
    return render(request, 'Home.html')

def server_list_viwe(request):
    server = Server.objects.all()
    context = {'server':server}
    return render(request, 'server_list.html', context)

def add_server_viwe(request):
    if request.method == "POST":
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('server_list')
    else:
        form = ServerForm() 

    context = {'form': form}
    return render(request, "add_server.html", context)        

def server_information_viwe(request):
    server_id = request.GET.get("id")
    if server_id:
        server = Server.objects.get(id=server_id)
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


