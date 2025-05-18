from django.shortcuts import render

# Create your views here.
def payment_page(request,booking_id):
    booking=Bookings.object
def success(request,booking_id)
    booking=Bookings.objects.get(id=booking_id)
    booking.booking_status='confirmed'
    booking.save()
    Payments.objects.create(booking=booking,payment_method='card,
                            amount=booking.total_amount,status='success')
    return render(request,'payments/success.html')

def cancel(request,booking_id):
    booking=Bookings.objects.get(id=booking_id)
    booking.booking_status='cancelled'
    booking.save()
    Payments.objects.create(booking=booking,payment_method='card',
                            amount=booking.total_amount,status='failed')
    return render(request,'payment')                        