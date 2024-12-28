from django.shortcuts import redirect, render

from old_items_app.forms import LoginRegisterForm, CustomerDetailsForm


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