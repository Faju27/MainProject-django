from django.shortcuts import redirect, render

from old_items_app.forms import LoginRegisterForm, SellerDetailsForm


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
