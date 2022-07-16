from django.contrib import admin
from .models import orders

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','numofproduct','startingdate','daycount',"appointmentdate")
    search_fields = ("name",)
    list_per_page = 20
    list_display_links = ("name",)

# Register your models here.



admin.site.register(orders,OrdersAdmin) 

