from django.contrib import  admin
from election.profile.models import UserProfile, City, Town

class UserProfileAdmin (admin.ModelAdmin):
    list_display = ('email','name', 'created_at',)



class CityAdmin (admin.ModelAdmin):
    list_display = ('name', 'code',)


class TownAdmin (admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Town, TownAdmin)