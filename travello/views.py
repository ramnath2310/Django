from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name ='Chennai'
    dest1.desc ='One of the hotest city in india'
    dest1.img='destination_1.jpg'
    dest1.offer =False
    dest1.price = 700

    dest2=Destination()
    dest2.name = "Mumbai"
    dest2.desc = "The city that never sleeps"
    dest2.img='destination_3.jpg'
    dest2.offer =False
    dest2.price =800

    dest3=Destination()
    dest3.name ='Kerala'
    dest3.desc ='It has beautiful nature'
    dest3.img='destination_2.jpg'
    dest3.offer =True
    dest3.price =900

    dests=[dest1,dest3,dest2]

    return render(request,"index.html",{'dests':dests})
    
    # return render(request, "index.html", {'dest1': dest1, 'dest2': dest2, 'dest3': dest3})
