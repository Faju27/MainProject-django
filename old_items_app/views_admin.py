from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from old_items_app.filters import AdminNameFilter
from old_items_app.forms import SellerDetailsForm
from old_items_app.models import Seller, Customer, Product


def login_page(request):
    if request.method == 'POST':
        user1 = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=user1, password=pass1)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            if user.is_customer:
                return redirect('customer_dashboard')
            elif user.is_seller:
                return redirect('seller_dashboard')
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, "admin/login.html")


@login_required(login_url='home')
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')


@login_required(login_url='home')
def seller_details_view(request):
    data = Seller.objects.all()
    return render(request, 'admin/seller_details.html', {'data': data})


@login_required(login_url='home')
def customer_details_view(request):
    data = Customer.objects.all()
    return render(request, 'admin/customer_details.html', {'data': data})


@login_required(login_url='home')
def seller_details_delete(request, id):
    data = Seller.objects.get(id=id)  # (pk=id)
    data.delete()
    return redirect('seller_details_view')


@login_required(login_url='home')
def customer_details_delete(request, id):
    data = Customer.objects.get(id=id)  # (pk=id)
    data.delete()
    return redirect('customer_details_view')


@login_required(login_url='home')
def seller_details_update(request, id):
    data = Seller.objects.get(id=id)
    form = SellerDetailsForm(instance=data)
    if request.method == 'POST':
        form1 = SellerDetailsForm(request.POST, request.FILES, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('seller_details_view')
    return render(request, "admin/seller_update.html", {'form': form})


@login_required(login_url='home')
def admin_product_view(request):
    data = Product.objects.all()
    admin_name_filter = AdminNameFilter(request.GET, queryset=data)
    data = admin_name_filter.qs
    return render(request, 'admin/all_products.html', {'data': data, 'admin_name_filter': admin_name_filter})


# detailed individual product information, for admin.
@login_required(login_url='home')
def admin_product_information(request, id):
    data = Product.objects.get(id=id)
    return render(request, "admin/admin_product_info.html", {'product_data': data})

