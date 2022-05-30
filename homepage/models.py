from django.db import models

# Create your models here.
class Mashina(models.Model):
    nomi = models.CharField(max_length=50, verbose_name='Mashina nomi')
    rangi = models.CharField(max_length=26)
    yili = models.DateTimeField()
    yili1 = models.DateField(verbose_name='Chiqarilgan yili')
    narxi = models.SmallIntegerField()
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.nomi

    class Meta:
        verbose_name = 'Mashina'
        verbose_name_plural = 'Mashinalar'