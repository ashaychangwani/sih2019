from django.contrib import admin

# Register your models her
# e.
from .models import Spares, Order

admin.site.register(Spares)
admin.site.register(Order)