from django.db import models

from django.contrib.auth.models import User
# Create your models here.
USER_1=1
USER_2=2

USER_ROLES=(
    (USER_1, 'SuperAdmin'),
    (USER_2, 'Guest'),

)



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField( max_length=30, blank=True)
    date_joined = models.DateTimeField( auto_now_add=True)
    role = models.SmallIntegerField(choices=USER_ROLES, default=USER_2)



