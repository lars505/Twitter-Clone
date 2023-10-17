from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default="Hola, putitos!", max_length=100)
    image =models.ImageField(default='default.jpg')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    

class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # ordenamos los post en cuestion de tiempo, el ultimo se muestra de primero
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return  self.content
