from django.db import models
from . GetRandomCode import get_shortned_url

# Create your models here.
class Shortner(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    total_clicks = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    #QRCode = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):

        if not self.short_url:
            self.short_url = get_shortned_url(self)
            #self.QRCode = get_qr_code(self)
        
        super().save(*args, **kwargs)
    