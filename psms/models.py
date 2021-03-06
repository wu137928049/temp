from django.db import models

# Create your models here.
class Users(models.Model):
    u_name = models.CharField(max_length=5)
    u_password = models.CharField(max_length=255)
    u_ticket = models.CharField(max_length=30, null=True)
    u_icon = models.ImageField(
        upload_to="icon",
        default='icon/default.png',
    )
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'zcdl'
        unique_together = ('u_name',)

class Service_line(models.Model):
    u_name = models.CharField(max_length=30)
    favor = models.ManyToManyField('Users')
    class Meta:
        db_table = 'ywx'

class service_summary(models.Model):
    yew = models.CharField(max_length=30)
    y_url = models.CharField(max_length=30)
    class Meta:
        db_table = 'zywx'
