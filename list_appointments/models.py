from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RolesUser(models.Model):
    ROLES_TYPE = (
        ("doctor", "Doctor"),
        ("paciente", "Paciente"),
    )

    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    rol = models.CharField(choices=ROLES_TYPE, max_length=20)

    class Meta:
        verbose_name = ("Custom User")
        verbose_name_plural = ("Custom Users")

    def __str__(self):
        return self.user.username


class CustomSettings(models.Model):
    SECTIONS = (
        ("SECTION_LOGIN",'Login'),
        ("SECTION_RPM_EMAIL",'RPM Email'),
        ("SECTION_TELEHEALTH_EMAIL",'TELEHEALTH Email'),
        ("SECTION_DASHBOARD",'Dashboard'),
    )


    id_provider = models.SmallIntegerField()  
    id_secction = models.CharField(choices=SECTIONS, max_length=100)
    configurations = models.JSONField() 
    photo = models.ImageField()  

    def __str__(self):        
        return "{}".format(self.id_secction)