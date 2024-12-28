from django.urls import path

from old_items_app import views, views_customer, views_seller, views_admin

urlpatterns = [
    path("", views.home, name='home'),
    # path("register", views.register_page, name='register_page'),


    #customer
    path("customer_register", views_customer.customer_details_add, name='customer_details_add'),


    #seller
    path("seller_register", views_seller.seller_details_add, name='seller_details_add'),


    #admin
    path("login", views_admin.login_page, name='login'),
    path("admin_view", views_admin.admin_details_view, name='admin_details_view'),
    path("seller_view", views_admin.seller_details_view, name='seller_details_view'),
    path("customer_view", views_admin.customer_details_view, name='customer_details_view'),
    path("seller_delete/<int:id>/", views_admin.seller_details_delete, name="seller_details_delete"),
    path("customer_delete/<int:id>/", views_admin.customer_details_delete, name="customer_details_delete"),
]
