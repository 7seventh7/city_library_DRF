from django.contrib import admin

from .models import *

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'time_create')

    # def save_model(self, request, obj, form, change):
    #     if 'age' in form.changed_data:
    #         raise self.ValidationError('age chenged!')
    #         print("age chenged")
    #     else:
    #         print("age not changed")
    #     super().save_model(request, obj, form, change)

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Person, PersonAdmin)
