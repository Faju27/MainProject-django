from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from old_items_app.filters import NameFilter
from old_items_app.forms import LoginRegisterForm, CustomerDetailsForm, CommentForm
from old_items_app.models import Product, Customer, Cart, MyStatus, Chat, Seller, Comment


def customer_details_add(request):
    form1 = LoginRegisterForm()
    form2 = CustomerDetailsForm()
    if request.method == 'POST':
        form1 = LoginRegisterForm(request.POST)
        form2 = CustomerDetailsForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_customer = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('/')

    return render(request, "customer/customer_register.html", {"form1": form1, "form2": form2})


# for all products view.search bar
@login_required(login_url='home')
def customer_dashboard(request):
    data = Product.objects.all()
    name_filter = NameFilter(request.GET, queryset=data)
    data = name_filter.qs
    return render(request, 'customer/customer_dashboard.html', {'data': data, 'name_filter': name_filter})


# product added to cart
@login_required(login_url='home')
def add_to_cart(request, id):
    product_data = Product.objects.get(id=id)
    user_data = request.user
    customer_data = Customer.objects.get(user=user_data)
    cart_items = Cart.objects.filter(product_details=product_data, customer_details=customer_data)
    if cart_items.exists():
        messages.error(request, 'This Product Already Existed')
        return redirect('customer_dashboard')
    else:
        cart_data = Cart()
        cart_data.product_details = product_data
        cart_data.customer_details = customer_data
        cart_data.save()
        messages.success(request, 'Product Added to Cart Successfully')
        return redirect('customer_dashboard')
    return render(request, 'customer/customer_dashboard.html')


# cart page
@login_required(login_url='home')
def cart(request):
    user_data = request.user
    customer_data = Customer.objects.get(user=user_data)
    cart_data = Cart.objects.filter(customer_details=customer_data)
    return render(request, 'customer/cart.html', {'data': cart_data})


# products remove from cart
@login_required(login_url='home')
def remove_from_cart(request, id):
    cart_data = Cart.objects.get(pk=id)
    cart_data.delete()
    return redirect('cart')


# detailed individual product information, for customer.
@login_required(login_url='home')
def customer_product_information(request, id):
    form = CommentForm()  # for comment
    user_data = request.user
    customer_data = Customer.objects.get(user=user_data)
    product_data = Product.objects.get(id=id)
    status_data = MyStatus.objects.filter(customer_details=customer_data, product_details=id)
    chat_data = Chat.objects.filter(product_details=product_data, customer_details=customer_data)
    seller_data = Seller.objects.get(id=product_data.seller_details.id)
    comment_data = Comment.objects.filter(product_details=product_data)

    reply = request.POST.get('reply')  # for chat reply
    if request.method == "POST":
        form1 = CommentForm(request.POST)

        for data in chat_data:  # for chat reply
            if data == chat_data.last():
                data.customer_message = reply
                data.save()
        if form1.is_valid():  # for comment
            obj = form1.save(commit=False)
            obj.product_details = product_data
            obj.seller_details = seller_data
            obj.customer_details = customer_data
            obj.save()
            # print(obj.customer_comment)
            return redirect('customer_product_information', id=id)
    return render(request, "customer/customer_product_info.html", {'product_data': product_data, 'status_data': status_data, 'chat_data': chat_data, 'form':form, 'comment_data':comment_data})


@login_required(login_url='home')
def customer_comment_delete(request, id):
    comment_data = Comment.objects.get(id=id)
    comment_data.delete()
    return redirect('customer_product_information', id=comment_data.product_details.id)


@login_required(login_url='home')
def status_buy(request, id):
    user_data = request.user
    customer_data = Customer.objects.get(user=user_data)
    product_data = Product.objects.get(id=id)
    status_data = MyStatus()
    status_data.product_details = product_data
    status_data.customer_details = customer_data
    status_data.save()
    return redirect('customer_product_information', id=id)
