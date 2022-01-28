from django.contrib import admin

# Register your models here.
from lawnote.models import Users

class UsersAdmin(admin.ModelAdmin):
  search_fields=('PrevD' , 'NextD' , 'Names' , )
  list_display=('PrevD', 'Names', 'NextD')

admin.site.register(Users,UsersAdmin)