from django.contrib import admin

from old_items_app import models

# Register your models here.
admin.site.register(models.LoginView)
admin.site.register(models.Customer)
admin.site.register(models.Seller)
admin.site.register(models.Product)
admin.site.register(models.Cart)
admin.site.register(models.MyStatus)