from django.shortcuts import render
from movies.models import movies
from accounts.models import User
from bookings.models import Bookings,bookingseats
from payments.models import Payments
from django.contrib.auth.decorators import login_required
# Create your views here.


def movies_listview(request):
    
    context ={
        'movies': movies.objects.all()
    }
    return render(request, 'movies/movies.html', context)




def movies_by_genre(request, genre):
    movie_list = movies.objects.filter(genre__iexact=genre)
    return render(request, 'movies/movies.html', {
        'movies': movie_list,
        'selected_genre': genre,
    })
def home(request):
    movies=Movies.objects.all()
    context={'movies':movies}
    return render(request,'dashboard/home.html',context)
@login_required
def your_orders(request):
    user=User.objects.get(username=request.user)
    bookings=Bookings.objects.filter(user=user,booking_status='confirmed').order_by('booking_time')
    tickets={payments.objects.get(booking-booking):BookingSeats.objects.filter(booking-booking)
             context={
                 'tickets':tickets,
                 'user':user,
             }
             return render(request,'dashboard/your_orders.html',context)}