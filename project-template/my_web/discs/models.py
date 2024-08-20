from django.db import models


class Disc(models.Model):
    name = models.CharField(max_length=20)
    speed = models.IntegerField()
    glide = models.IntegerField()
    turn = models.IntegerField()
    fade = models.IntegerField()
    image = models.ImageField(default='default_disc.webp', upload_to='disc_images/', null=True, blank=True)
