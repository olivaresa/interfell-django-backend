from django.contrib import admin
from users.models import Cities, Countries, AcademicLevels, User

class CitiesAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cities, CitiesAdmin)

class CountriesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Countries, CountriesAdmin)

class AcademicLevelsAdmin(admin.ModelAdmin):
    pass
admin.site.register(AcademicLevels, AcademicLevelsAdmin)


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
