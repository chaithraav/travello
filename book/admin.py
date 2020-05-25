from django.contrib import admin
from .models import Places,reservation,Payment
# Register your models here.
admin.site.register(Places)
admin.site.register(reservation)
admin.site.register(Payment)