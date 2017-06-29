from django.contrib import admin
from .models import Flower as f
from .models import Honeycomb as hc
from .models import Honey as h

class fAdmin(admin.ModelAdmin):
		list_display = ('id', 'name')

admin.site.register(f, fAdmin)
admin.site.register(hc)
admin.site.register(h)


# Register your models here.
