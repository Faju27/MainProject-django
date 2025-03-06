from django.urls import path

from old_items_app import views, views_customer, views_seller, views_admin

urlpatterns = [
    path("", views.home, name='home'),
    path("logout", views.logout_view, name='logout'),

    # customer
    path("customer_register", views_customer.customer_details_add, name='customer_details_add'),
    path("customer_dashboard", views_customer.customer_dashboard, name='customer_dashboard'),
    path("add_to_cart/<int:id>/", views_customer.add_to_cart, name='add_to_cart'),
    path("cart", views_customer.cart, name='cart'),
    path("remove_from_cart/<int:id>/", views_customer.remove_from_cart, name='remove_from_cart'),
    path("customer_product_information/<int:id>/", views_customer.customer_product_information, name='customer_product_information'),
    path("customer_comment_delete/<int:id>/", views_customer.customer_comment_delete, name='customer_comment_delete'),
    path("status_buy/<int:id>/", views_customer.status_buy, name='status_buy'),

    # seller
    path("seller_register", views_seller.seller_details_add, name='seller_details_add'),
    path("seller_dashboard", views_seller.seller_dashboard, name='seller_dashboard'),
    path("product_register", views_seller.product_details_add, name='product_details_add'),
    path("product_view", views_seller.product_view, name='product_view'),
    path("product_delete/<int:id>/", views_seller.product_delete, name='product_delete'),
    path("product_update/<int:id>/", views_seller.product_update, name='product_update'),
    path("seller_product_information/<int:id>/", views_seller.seller_product_information, name='seller_product_information'),
    path("seller_comment_delete/<int:id>/", views_seller.seller_comment_delete, name='seller_comment_delete'),
    path("request_view", views_seller.request_view, name='request_view'),
    path("request_accept/<int:id>/", views_seller.request_accept, name='request_accept'),
    path("request_reject/<int:id>/", views_seller.request_reject, name='request_reject'),
    path("message_to_customer/<int:id>/", views_seller.message_to_customer, name='message_to_customer'),


    # admin
    path("login", views_admin.login_page, name='login'),
    path("admin_dashboard", views_admin.admin_dashboard, name='admin_dashboard'),
    path("seller_view", views_admin.seller_details_view, name='seller_details_view'),
    path("customer_view", views_admin.customer_details_view, name='customer_details_view'),
    path("seller_delete/<int:id>/", views_admin.seller_details_delete, name="seller_details_delete"),
    path("customer_delete/<int:id>/", views_admin.customer_details_delete, name="customer_details_delete"),
    path("seller_update/<int:id>/", views_admin.seller_details_update, name="seller_details_update"),
    path("admin_product_view", views_admin.admin_product_view, name='admin_product_view'),
    path("admin_product_information/<int:id>/", views_admin.admin_product_information, name='admin_product_information')

]
