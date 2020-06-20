from django.contrib import admin
from .models import Questions, Choices, Answer

admin.site.register(Questions)
admin.site.register(Choices)
admin.site.register(Answer)
