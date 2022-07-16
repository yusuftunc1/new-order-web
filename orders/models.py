
from django.db import models

# Create your models here.

class orders(models.Model):
    name = models.CharField(max_length=45, verbose_name="Kullanıcı Adı")
    email = models.EmailField(verbose_name="Mail")
    numofproduct = models.IntegerField(verbose_name="Koli Adeti")
    startingdate = models.DateField(verbose_name="Resim Atma Tarihi")
    appointmentdate = models.DateField(blank=True,null=True, verbose_name="Randevu Tarihi")
    daycount = models.IntegerField(blank=True, null=True, verbose_name="Kurumada Geçen Gün")
    remainingday = models.IntegerField(blank=True, null=True, verbose_name="Kalan Gün")
    note = models.TextField(blank=True, null=True, verbose_name="Not")
    created_date = models.DateField(auto_now_add= True)
    userid = models.IntegerField(verbose_name= "Kullanıcı Id")

    def __str__(self):
        return self.name



