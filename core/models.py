from django.db import models
from django.utils.translation import gettext as _  

LANGUAGE_LEVEL_CHOICES = [
    (1, 'Elémentaire'), (2, 'Pré-intermédiaire'), (3, 'Intermédiaire'), (4, 'Courrant')
]

# Create your models here.
class Language(models.Model):
    name = models.CharField(_("Language"), max_length=50)
    level_1 = models.CharField(_("Level 1"), max_length=50)
    level_2 = models.CharField(_("Level 2"), max_length=50)
    level_3 = models.CharField(_("Level 3"), max_length=50)
    level_4 = models.CharField(_("Level 4"), max_length=50)

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
