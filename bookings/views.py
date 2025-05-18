from django.shortcuts import render
from theatre.models import theatre, showtimes, seats
from movies.models import movies
from accounts.models import User
from datetime import datetime, timedelta
# Create your views here.

def theatre_show_time_view(request, slug):
    today = datetime.today().date()
    start_date = today-timedelta(days=0)
    week=[]
    for i in range(7):
        day=start_date+timedelta(days=i)
        week.append({
            'name' : day.strftime('%a').upper(),
            'day' : day.day,
            'month' : day.strftime('%b').upper(),
            'date' : day

        })



    if movies.objects.filter(slug=slug).exists():
        movie = movies.objects.get(slug=slug)
        theatre_showtimes=[
            showtimes.objects.filter(movie=movie, theatre=theatre_obj).order_by('show_time')
            for theatre_obj in theatre.objects.all() if showtimes.objects.filter(movie=movie, theatre=theatre_obj).exists()]
        context = {
            'theatre_showtimes': theatre_showtimes,
            'm': movie,
            'week': week,
            'today': today,

        }
        return render(request, 'theatre/theatre_show_time.html', context)
    return render(request, 'movies/404.html' )    

def seat_selection_views(request,showtime_id):
    showtime=Showtimes.objects.get(id=showtime_id)
    all_seats=Seats.objects.filter(
        theater=showtime.theater,
        screen_number=showtime.screen_number
    ).order_by('row_label','seat_number')

    seat_rows={}
    for seat in all_seats:
        row = seat.row_label
        if row not in seat_rows:
            seat_rows[row]=[]
        seat_rows[row].append(seat)

    context={
        'showtime':showtime,
        'seat_rows':seat_rows,
    }        
    return render(request,'theater/seating.html',context)
