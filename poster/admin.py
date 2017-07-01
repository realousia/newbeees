from django.contrib import admin
from .models import Flower as f
from .models import Honeycomb as hc
from .models import Honey as h
from .models import Seed as s

class fAdmin(admin.ModelAdmin):
		list_display = ('id', 'name')

admin.site.register(s, fAdmin)
admin.site.register(f, fAdmin)
admin.site.register(hc, fAdmin)
admin.site.register(h, fAdmin)


# Register your models here.
