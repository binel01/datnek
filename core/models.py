from django.db import models
from django.utils.translation import gettext_lazy as _  

LANGUAGE_LEVEL_CHOICES = [
    (1, _('Elémentaire')), (2, _('Pré-intermédiaire')), (3, _('Intermédiaire')), (4, _('Courrant'))
]

# Create your models here.
class Language(models.Model):
    name = models.CharField(_("Language"), max_length=50)
    level_1 = models.CharField(_("Niveau 1"), max_length=50)
    level_2 = models.CharField(_("Niveau 2"), max_length=50)
    level_3 = models.CharField(_("Niveau 3"), max_length=50)
    level_4 = models.CharField(_("Niveau 4"), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'   

class LanguageLevel(models.Model):
    language = models.ForeignKey("Language", verbose_name=_("Language"), on_delete=models.CASCADE)
    speaking_level = models.IntegerField(_("Speaking"), choices=LANGUAGE_LEVEL_CHOICES)
    writting_level = models.IntegerField(_("Writting"), choices=LANGUAGE_LEVEL_CHOICES)
    understanding_level = models.IntegerField(_("Understanding"), choices=LANGUAGE_LEVEL_CHOICES)

    def __str__(self):
        return str(self.language) + ': ' + str(self.speaking_level) + ' - ' + str(self.writting_level) \
            + ' - ' + str(self.understanding_level)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'LanguageLevel'
        verbose_name_plural = 'LanguageLevels'
