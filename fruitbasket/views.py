from fruitbasket.models import Destination
from django.shortcuts import redirect, render
from .models import Destination
# Create your views here.
# database through pass data
def index(request):
    dests = Destination.objects.all()
    return render(request,"index.html",{'dests':dests})

def post(request):
    product = request.POST.get('product')
    print(product)
    return redirect('index')
    


"""
def index(request):

    dest1 = Destination()
    dest1.name = 'Bell Pepper'
    dest1.price = 44
    dest1.img = 'product-1.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'STRAWBERRY'
    dest2.price = 52
    dest2.img = 'product-2.jpg'
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'GREEN BEANS'
    dest3.price = 77
    dest3.img = 'product-3.jpg'
    dest3.offer = True
    
    dest4 = Destination()
    dest4.name = 'PURPLE CABBAGE'
    dest4.price = 65
    dest4.img = 'product-4.jpg'
    dest4.offer = True

    dest5 =Destination()
    dest5.name = 'BEAT ROOT'
    dest5.price = 25
    dest5.img = 'product-15.jpg'
    dest5.offer = False

    dest6 = Destination()
    dest6.name = 'TOMATOS'
    dest6.price = 33
    dest6.img = 'product-5.jpg'
    dest6.offer = False

    dest7 = Destination()
    dest7.name = 'BROCOLLI'
    dest7.price = 47
    dest7.img = 'product-6.jpg'
    dest7.offer = True
    
    dest8 = Destination()
    dest8.name = 'CARROTS'
    dest8.price = 12
    dest8.img = 'product-7.jpg'
    dest8.offer = False

    dest9 = Destination()
    dest9.name = 'ONION'
    dest9.price = 22
    dest9.img = 'product-9.jpg'
    dest9.offer = True
    
    dest10 = Destination()
    dest10.name = 'APPLE'
    dest10.price = 120
    dest10.img = 'product-10.jpg'
    dest10.offer = True
    
    dest11 = Destination()
    dest11.name = 'RED CHILLI'
    dest11.price = 63
    dest11.img = 'product-11.jpg'
    dest11.offer = False
   
    dest12 = Destination()
    dest12.name = 'GARLIC'
    dest12.price = 95
    dest12.img = 'product-12.jpg' 
    dest12.offer = False

    dest13 = Destination()
    dest13.name = 'POTATO'
    dest13.price = 15
    dest13.img = 'product-14.jpeg'
    dest13.offer = True

    dest14 = Destination()
    dest14.name = 'CAULI FLOWER'
    dest14.price = 8
    dest14.img = 'flawer.jpg'
    dest14.offer = False

    dest15 = Destination()
    dest15.name = 'CABBAGE'
    dest15.price = 17
    dest15.img = 'Cabbage.jpeg'
    dest15.offer = False

    dest16 = Destination()
    dest16.name = 'BANANA'
    dest16.price = 30
    dest16.img = 'banana1.png'
    dest16.offer = True

   

    dests =[dest1,dest2,dest3,dest4,dest5,dest6,dest7,dest8,dest9,dest10,dest11,dest12,dest13,dest14,dest15,dest16]
    return render(request,"index.html",{'dests':dests})
"""