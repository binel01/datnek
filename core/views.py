from django.shortcuts import render
from django.views.generic import CreateView
from .models import LanguageLevel, LANGUAGE_CHOICES, LANGUAGE_LEVEL_CHOICES

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

        # Convertir les niveaux de langues avant de les envoyer au template
        for level in language_levels:
            level.language = LANGUAGE_CHOICES[level.language - 1][1]
            level.speaking_level = LANGUAGE_LEVEL_CHOICES[level.speaking_level - 1][1]
            level.writting_level = LANGUAGE_LEVEL_CHOICES[level.writting_level - 1][1]
            level.understanding_level = LANGUAGE_LEVEL_CHOICES[level.understanding_level - 1][1]
        
        home = {
            'level_count': level_count,
            'language_levels': language_levels
        }
        context["home"] = home
        return context