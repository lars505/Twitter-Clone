from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default="Hola, putitos!", max_length=100)
    image =models.ImageField(default='default.jpg')

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def following(self):
        user_id = Relationships.objects.filter(from_user=self.user)\
                                       .values_list('to_user_id', flat=True) 

        return User.objects.filter(id__in=user_id)        
    
    def followers(self):
        user_id = Relationships.objects.filter(to_user=self.user)\
                                       .values_list('from_user_id', flat=True) 

        return User.objects.filter(id__in=user_id)        
    

class Post(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    # ordenamos los post en cuestion de tiempo, el ultimo se muestra de primero
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return  self.content


class Relationships(models.Model):
    from_user = models.ForeignKey(User, related_name="relationsships", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="related_to", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.from_user} to {self.to_user}'
    