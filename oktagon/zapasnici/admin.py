from django.contrib import admin
from .models import Sponsors
from .models import Fighter
from .models import Organisation
from .models import Tournaments

admin.site.register(Sponsors)
admin.site.register(Fighter)
admin.site.register(Organisation)
admin.site.register(Tournaments)