from django.contrib import  admin
from election.profile.models import UserProfile, City, Town

class UserProfileAdmin (admin.ModelAdmin):
    list_display = ('email','name', 'created_at',)


def get_cities_and_towns():
    print("Dosya import edeceğim")


class CityAdmin (admin.ModelAdmin):
    list_display = ('name', 'code',)


    def import_cities_and_towns(modeladmin, request, queryset):
        get_cities_and_towns()

    actions = [import_cities_and_towns, ]

    import_cities_and_towns.short_description = "İl ve ilçeleri Yükle"



class TownAdmin (admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Town, TownAdmin)