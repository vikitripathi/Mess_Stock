from django.contrib import admin
from stockAPI.models import Items,Units,Transactions

# Register your models here.
admin.site.register(Items)
admin.site.register(Units)
admin.site.register(Transactions)
