from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from old_items_app.filters import NameFilter
from old_items_app.forms import LoginRegisterForm, SellerDetailsForm, ProductForm, ChatForm, CommentForm
from old_items_app.models import Seller, Product, MyStatus, Customer, Chat, Comment


# seller registration
def seller_details_add(request):
    form1 = LoginRegisterForm()
    form2 = SellerDetailsForm()
    if request.method == 'POST':
        form1 = LoginRegisterForm(request.POST)
        form2 = SellerDetailsForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_seller = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect('/')

    return render(request, "seller/seller_register.html", {"form1": form1, "form2": form2})


# seller home page
@login_required(login_url='home')
def seller_dashboard(request):
    user_data = request.user
    seller_data = Seller.objects.get(user=user_data)
    return render(request, 'seller/seller_dashboard.html', {'seller_data': seller_data})


# product add
@login_required(login_url='home')
def product_details_add(request):
    user_data = request.user
    seller_data = Seller.objects.get(user=user_data)
    form = ProductForm()
    if request.method == 'POST':
        form1 = ProductForm(request.POST, request.FILES)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.seller_details = seller_data
            obj.save()
            return redirect('product_view')

    return render(request, "seller/product_register.html", {"form": form, 'seller_data': seller_data})


# product view
@login_required(login_url='home')
def product_view(request):
    user_data = request.user
    seller_data = Seller.objects.get(user=user_data)
    product_data = Product.objects.filter(seller_details=seller_data)
    return render(request, 'seller/my_products.html', {'data': product_data, 'seller_data': seller_data})


# for product delete.
@login_required(login_url='home')
def product_delete(request, id):
    data = Product.objects.get(id=id)
    data.delete()
    return redirect('product_view')


# product update.
@login_required(login_url='home')
def product_update(request, id):
    user_data = request.user
    seller_data = Seller.objects.get(user=user_data)
    data = Product.objects.get(id=id)
    form = ProductForm(instance=data)
    if request.method == 'POST':
        form1 = ProductForm(request.POST, request.FILES, instance=data)
        if form1.is_valid():
            form1.save()
            return redirect('product_view')

    return render(request, 'seller/product_update.html', {'form': form, 'seller_data': seller_data})


# detailed individual product information, for seller.
@login_required(login_url='home')
def seller_product_information(request, id):
    form = CommentForm()
    product_data = Product.objects.get(id=id)
    comment_data = Comment.objects.filter(product_details=product_data)
    reply = request.POST.get('reply')
    if request.method == 'POST':
        for data in comment_data:
            if data == comment_data.last():
                data.seller_comment = reply
                data.save()
                return redirect('seller_product_information', id=id)
    return render(request, "seller/seller_product_info.html", {'product_data': product_data, 'comment_data': comment_data})


@login_required(login_url='home')
def seller_comment_delete(request, id):
    comment_data = Comment.objects.get(id=id)
    comment_data.delete()
    return redirect('seller_product_information', id=comment_data.product_details.id)


@login_required(login_url='home')
def request_view(request):
    user_data = request.user
    seller_data = Seller.objects.get(user=user_data)
    request_data = MyStatus.objects.filter(product_details__seller_details=seller_data)
    return render(request, "seller/customer_request.html", {'seller_data': seller_data, 'request_data': request_data})


@login_required(login_url='home')
def request_accept(request, id):
    status_data = MyStatus.objects.get(id=id)
    status_data.status = 1
    status_data.save()
    return redirect('request_view')


@login_required(login_url='home')
def request_reject(request, id):
    status_data = MyStatus.objects.get(id=id)
    status_data.status = 2
    status_data.save()
    return redirect('request_view')


@login_required(login_url='home')
def message_to_customer(request, id):
    form = ChatForm()
    user_data = request.user
    seller_data = Seller.objects.get(user=user_data)
    status_data = MyStatus.objects.get(id=id)
    customer_data = status_data.customer_details
    product_data = status_data.product_details
    chat_data = Chat.objects.filter(status_details=status_data)
    if request.method == 'POST':
        form1 = ChatForm(request.POST)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.product_details = product_data
            obj.seller_details = seller_data
            obj.customer_details = customer_data
            obj.status_details = status_data
            obj.save()
            return redirect('message_to_customer', id=id)
        else:
            print("error....", form1.errors)
    return render(request, 'seller/chat_with_customer.html', {'form': form, 'chat_data': chat_data, 'customer_data': customer_data, 'product_data': product_data})
