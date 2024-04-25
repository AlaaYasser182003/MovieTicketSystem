from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate , login
from Cinema.models import Movie, Showtime, reservations, Seat, Payment
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.db.models import Sum
from django.contrib.sessions.models import Session

# Create your views here.
def registration(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exist')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exist')
            else:        
                user = User.objects.create_user(username = username, first_name= first_name, last_name= last_name, email=email,password=password1)
                user.save()
                messages.info(request,'User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not match')
        return redirect('registration')                 
    else:
        return render(request,"Cinema/registration.html")


def user_login(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user =authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,"Cinema/Home.html") 
        
        else:
            return render(request, "Cinema/registration.html",{
                "messsage": "Invalid credentials,  please Register First"
            })
        
    return render(request, "Cinema/login.html")

def home(request):
    
    return render(request, "Cinema/Home.html",{
      "movies": Movie.objects.all()
  })
   

def details(request, key):
   movie =Movie.objects.get(pk=key)
   return render(request,"Cinema/details.html",{
      'movie':movie, 
      "movie_show":movie.movie_show.all()
      })
    
def seat(request, key,shows):
  showtime =Showtime.objects.get(pk=shows)
  movie=Movie.objects.get(pk=key)
 # seat =reservations.objects.filter(pk=shows)
  return render(request,"Cinema/seat.html",{
      'showtime': showtime, 
      'movie':movie, 
      "seats":Seat.objects.all()
  }
 )

def admin(request):
    return render(request,"admin/")

def reservation(request, key):
    movie=Movie.objects.get(pk=key)
    user = request.user
    book = reservations.objects.filter(user=user.pk)
    return render(request,"Cinema/payment.html", {'book':book, 
    'movie':movie} )
      
def payment(request,key, shows,seats):
     seatno=Seat.objects.get(pk=seats)
     movie=Movie.objects.get(pk=key)
     showtime=Showtime.objects.get(pk=shows)
     return render(request, "Cinema/payment.html",{
         'movie':movie, 'showtime':showtime,
         "seatno":seatno
     })

def ticket(request, key,shows,seats):
   showtime =Showtime.objects.get(pk=shows)
   movie=Movie.objects.get(pk=key)
   useat=Seat.objects.get(pk=seats)
   if request.method == 'POST':
    card_name = request.POST['cardname']
    card_number = request.POST['cardnumber']
    exp_month = request.POST['expmonth']
    exp_year= request.POST['expyear']
    ucvv = request.POST['cvv']
             
    payment= Payment.create(cardname=card_name,cardnumber=card_number,expmonth=exp_month,expyear=exp_year,cvv=ucvv)
    payment.save()
    return render(request,"Cinema/ticket.html",{
        'showtime':showtime, 
        'movie':movie,
        "useat":useat
       # "user": User.objects.get(pk=pk).username
    })
   return render(request,"Cinema/ticket.html",{
        'showtime':showtime, 
        'movie':movie,
        'useat':useat})
    

