from django.db import models
from django.urls import reverse
# Create your models here.
class Rock(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):

        return reverse('rocks')

    def __str__(self):
        return '%s %s' % (self.name, self.description)
