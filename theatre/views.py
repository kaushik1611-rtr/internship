from django.shortcuts import render
from .models import theatre


# Create your views here.
def theater_show_time_selected_date_view(request,slug,date_str):
    try:
        selected_date=datetime.strptime(date_str,'%Y-%m-%d').date()
    except ValueError:
        selected_date=datetime.today().date()
        today=datetime.today().date()
        start_date=today-timedelta(days=0)
        week=[]
        for i in range(7):
            day=start_date=timedelta(days=i)
            week.append({
                'name':day.strftime("%a").upper(),
                'day':day.day,
                'month':day.strftime("%b").upper(),
                'date':day
            })
if Movies.objects.filter(slug=slug).exists():
    movie=Movies.objects.get(slug=slug)
    theater_showtimes=[
        Showtimes.objects.filter(movie=movie,theater=theater,show_time__date=selected_date).order_by('show_time')
    ]