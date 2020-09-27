from django.contrib import admin
from .models import user_profile, Post

# Register your models here.

class user_profile_admin(admin.ModelAdmin):
    fieldsets = [
        ("NAME", {"fields":["fname","mname","lname"]}),
        ("DONATION DETAIL",{"fields":["donation_date","quantity","itemname"]})
    ]
admin.site.register(user_profile,user_profile_admin)
class Post_admin(admin.ModelAdmin):
    fieldsets = [
        ("USER", {"fields":["fullname","email",]}),
        ("DONATION DETAIL",{"fields":["quantity","itemname"]}),
        ("USER ADDRESS", {"fields":["city","state","zipcode"]}),
    ]
admin.site.register(Post,Post_admin)
