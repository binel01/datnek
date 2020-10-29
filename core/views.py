from django.shortcuts import render
from django.views.generic import CreateView
from .models import Language, LanguageLevel

class LanguageLevelCreateView(CreateView):
    model = LanguageLevel
    template_name = "core/index.html"
    fields = '__all__'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Récupération du nombre de LanguageLevels
        level_count = LanguageLevel.objects.count()
        # Récupération de tous les LanguageLevels
        language_levels = LanguageLevel.objects.all()
        # Récupération de toutes les langues
        languages = Language.objects.all()
        
        home = {
            'level_count': level_count,
            'languages': languages, 
            'language_levels': language_levels
        }
        context["home"] = home
        return context