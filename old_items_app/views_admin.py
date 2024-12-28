from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from old_items_app.models import Seller, Customer


def login_page(request):
    if request.method == 'POST':
        user1 = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=user1, password=pass1)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_details_view')
            if user.is_customer:
                return redirect('customer_details_view')
            elif user.is_seller:
                return redirect('seller_details_view')
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, "admin/login.html")


def admin_details_view(request):
    return render(request, 'admin/admin_dashboard.html')


def seller_details_view(request):
    data = Seller.objects.all()
    return render(request, 'admin/seller_dashboard.html', {'data': data})


def customer_details_view(request):
    data = Customer.objects.all()
    return render(request, 'admin/customer_dashboard.html', {'data': data})


def seller_details_delete(request, id):
    data = Seller.objects.get(id=id)  # (pk=id)
    data.delete()
    return redirect('seller_details_view')


def customer_details_delete(request, id):
    data = Customer.objects.get(id=id)  # (pk=id)
    data.delete()
    return redirect('customer_details_view')
