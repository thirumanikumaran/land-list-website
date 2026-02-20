from django.db import models


class Land(models.Model):
    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
        default=""
    )

    owner_name = models.CharField(
        max_length=100,
        default="Unknown"
    )

    owner_phone = models.CharField(
        max_length=15,
        default="Unknown"
    )

    price = models.FloatField()

    area_sqft = models.IntegerField()

    # ✅ Multiple Images
    image1 = models.ImageField(
        upload_to='lands/',
        blank=True,
        null=True
    )
    image2 = models.ImageField(
        upload_to='lands/',
        blank=True,
        null=True
    )
    image3 = models.ImageField(
        upload_to='lands/',
        blank=True,
        null=True
    )
    image4 = models.ImageField(
        upload_to='lands/',
        blank=True,
        null=True
    )
    image5 = models.ImageField(
        upload_to='lands/',
        blank=True,
        null=True
    )

    # ✅ Map Location
    latitude = models.FloatField(
        blank=True,
        null=True,
        default=10.7870
    )

    longitude = models.FloatField(
        blank=True,
        null=True,
        default=78.7047
    )

    # ✅ Admin Display
    def __str__(self):
        return self.title