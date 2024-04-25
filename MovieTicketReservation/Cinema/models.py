from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

genre_choices = (
        ("Action","AC",),
        ("Comedy","CO" ),
        ( "Fantasy","FA"),
        ("Horror","HO"),
        ("Mystery","MY"),
        ( "Romance","RO"),
        ("Thriller","TH"),
        ( "Mystery","MY"),
        ( "Romance","RO",),
        ("Thriller","TH"),
        ("Unknown","Un")
)
language_choices =(
    ( "Arabic","Ar"), 
    ("English","En"),
    ("French","Fr"),
    ( "Chinese","Ch"),
    ("Korean","Ko"),
    ("Hindi","Hi")
)
country_choices=(
    ("Egypt","Eg"),
    ("United-states","US"),
    ("United Kingdom","UK"),
    ("India","In"),
    ("Korea","Ko"),
    ( "China","Ch")
)

class Movie(models.Model):
    key=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, default="")
    movie_poster =models.ImageField(upload_to='images/',default="images/unkonwn2.jpg")    # specify width and height
    cast = models.TextField()
   # image2=models.ImageField(default="cinema4.jpg")
    # poster =models.ForeignKey(Image, on_delete=models.CASCADE)
    genre =models.CharField(
        max_length =20,
        choices = genre_choices,
        default="Unknown"
    )
    
    language =models.CharField(
        max_length=15,
        choices =language_choices,
        default="Arabic"
    )
    country =models.CharField(
        max_length=20,
        choices=country_choices,
        default ="Egypt"
    )
    duration=models.DurationField(max_length=15)
    experience =models.CharField(max_length=15)
    threeD =models.BooleanField() 
    releaseYear =models.DateField()
    trailer= models.URLField()
    description =models.TextField()
    
 

class Showtime(models.Model):
    shows=models.AutoField(primary_key=True)
    movie_showtimes=models.ManyToManyField('Movie', related_name='movie_show' )
    date=models.DateField()
    time=models.CharField(max_length=100)
    price=models.IntegerField()


class reservations(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shows = models.ForeignKey(Showtime, on_delete=models.CASCADE)
    useat = models.CharField(max_length=100)

class Seat(models.Model):
   seats =models.AutoField(primary_key=True)
   seatno = models.CharField(max_length=10)

class Payment(models.Model):
    payment=models.AutoField(primary_key=True)
    cardname=models.CharField(max_length=20)
    cardno=models.CharField(max_length=16)
    expmonth=models.CharField(max_length=10)
    expyear=models.CharField(max_length=4)
    cvv=models.CharField(max_length=3)
    def create(cls, cardname, cardno,expmonth,expyear,cvv):
        payment=cls(cardname=cardname, cardno=cardno, expmonth=expmonth,expyear=expyear,cvv=cvv)
        return payment
   
    
    
    
       
    
















    
