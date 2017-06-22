from django.contrib import admin
from .models import Flower as f
from .models import Honeycomb as hc
from .models import Honey as h

admin.site.register(f)
admin.site.register(hc)
admin.site.register(h)


# Register your models here.
