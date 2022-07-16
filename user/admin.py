from django.contrib import admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email',)
    search_fields = ("name",)
    list_per_page = 20
    list_display_links = ("name",)