from django.contrib import admin
from .models import Language, LanguageLevel

# Register your models here.
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    pass
