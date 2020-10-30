from django.contrib import admin
from .models import LanguageLevel


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    pass
