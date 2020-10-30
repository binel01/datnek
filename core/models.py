from django.db import models
from django.utils.translation import gettext_lazy as _  

LANGUAGE_LEVEL_CHOICES = [
    (1, _('Elémentaire')), (2, _('Pré-intermédiaire')), (3, _('Intermédiaire')), (4, _('Courrant'))
]

LANGUAGE_CHOICES = [
    (1, _('Français')), (2, _('Anglais')), (3, _('Néerlandais'))
]


class LanguageLevel(models.Model):
    language = models.IntegerField(_("Langue"), choices=LANGUAGE_CHOICES)
    speaking_level = models.IntegerField(_("Parlé"), choices=LANGUAGE_LEVEL_CHOICES)
    writting_level = models.IntegerField(_("Ecrit"), choices=LANGUAGE_LEVEL_CHOICES)
    understanding_level = models.IntegerField(_("Compréhension"), choices=LANGUAGE_LEVEL_CHOICES)

    def __str__(self):
        return str(self.language) + ': ' + str(self.speaking_level) + ' - ' + str(self.writting_level) \
            + ' - ' + str(self.understanding_level)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'LanguageLevel'
        verbose_name_plural = 'LanguageLevels'
