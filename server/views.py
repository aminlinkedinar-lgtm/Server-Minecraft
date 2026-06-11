from django.shortcuts import render
from random import randint
# Create your views here.

def home_server_viwe(request):
    return render(request, 'Home.html')

def server_list_viwe(request):
    context = {'server_name':"darc_craft",
                'type':"AMIN",
                'ip':"12",
                'explain':"IRAN server",
                'some_player': "13",
                'gg':"good",
                'qq':"1405",
                'ss':"amin",    
                }
    return render(request, 'server_list.html', context)