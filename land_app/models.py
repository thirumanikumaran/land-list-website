from django.db import models

class Land(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")

    owner_name = models.CharField(max_length=100, default="unknown")
    owner_phone = models.CharField(max_length=15, default="unknown")

    price = models.FloatField()
    area_sqft = models.IntegerField()

    image1 = models.URLField()
    image2 = models.URLField(blank=True, null=True)
    image3 = models.URLField(blank=True, null=True)
    image4 = models.URLField(blank=True, null=True)
    image5 = models.URLField(blank=True, null=True)

    latitude = models.FloatField(null=True, blank=True, default=10.7870)
    longitude = models.FloatField(null=True, blank=True, default=78.7047)

    def __str__(self):
        return self.title
