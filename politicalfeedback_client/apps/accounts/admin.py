from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from apps.accounts.models import Profilo, Comune, Provincia

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class ProfiloInline(admin.StackedInline):
    model = Profilo
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfiloInline, )



class ComuneInline(admin.TabularInline):
    model = Comune
    extra = 6
    search_fields = ['comune']
    
class ProvinciaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['codice','provincia']}),
    ]
    inlines = [ComuneInline]
    search_fields = ['provincia']


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
