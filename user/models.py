from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CARGOS = ( ('Manager', 'Manager'),
            ('Logistics', 'Logistics'),
            ('Accountant', 'Accountant')
)
class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete = models.CASCADE)
    cc = models.IntegerField(default = 0)
    position = models.CharField(max_length = 20, choices = CARGOS, null = False, default = 'Accountant')
    image = models.ImageField(default='profile_images/kermit0.png', upload_to='profile_images')

    def __str__(self):
        return f'{self.profile.username} profile'