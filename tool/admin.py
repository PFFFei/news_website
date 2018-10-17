from django.contrib import admin

# Register your models here.
from .models import *

class InformationAdmin(admin.ModelAdmin):
    list_display = ('title','time','created')
class MilitaryAdmin(admin.ModelAdmin):
    list_display = ('title','time','created')
class SportsAdmin(admin.ModelAdmin):
    list_display = ('title','time','created')
class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ('title','time','created')
class FinanceAdmin(admin.ModelAdmin):
    list_display = ('title','time','created')


admin.site.register(Information,InformationAdmin)
admin.site.register(Military,MilitaryAdmin)
admin.site.register(Sports,SportsAdmin)
admin.site.register(Entertainment,EntertainmentAdmin)
admin.site.register(Finance,FinanceAdmin)
