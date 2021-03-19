from django.contrib import admin
from .models import *

# from .models import User
admin.site.register(Client)
# admin.site.register(Jobs)
admin.site.register(Job)
admin.site.register(SavedJobs)
admin.site.register(AppliedJobs)