from django.shortcuts import render, redirect
from .models import Registration

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        event_name = request.POST.get('event_name')

        Registration.objects.create(
            name=name,
            email=email,
            phone=phone,
            event_name=event_name
        )
        return redirect('success')
    return render(request, 'index.html')


def success(request):
    return render(request, 'success.html')


def view_registrations(request):
    data = Registration.objects.all().order_by('-created_at')
    return render(request, 'view_registrations.html', {'data': data})
