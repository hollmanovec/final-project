from django.db import models
from PIL import Image


class Disc(models.Model):
    DISC_TYPES = [
        ('Distance Driver', 'Distance Driver'),
        ('Fairway Driver', 'Fairway Driver'),
        ('Mid-Range', 'Mid-Range'),
        ('Putter', 'Putter'),
    ]

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=DISC_TYPES)
    brand = models.CharField(max_length=30)
    speed = models.IntegerField(default=1)
    glide = models.IntegerField(default=1)
    turn = models.IntegerField(default=0)
    fade = models.IntegerField(default=0)
    image = models.ImageField(default='default_disc.webp', upload_to='disc_images/', null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        super(Disc, self).save(**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
