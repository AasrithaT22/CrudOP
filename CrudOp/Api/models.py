from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Employee(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='employee')
    name = models.CharField(max_length=255)
    salary = models.IntegerField()
    role = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    TRANSPORT_CHOICE_CAR = 'C'
    TRANSPORT_CHOICE_BIKE = 'B'
    TRANSPORT_CHOICE_SHUTTLE = 'S'
    TRANSPORT_CHOICES = [
        (TRANSPORT_CHOICE_CAR, 'CAR'),
        (TRANSPORT_CHOICE_BIKE, 'BIKE'),
        (TRANSPORT_CHOICE_SHUTTLE, 'SHUTTLE'),
    ]
    mode_of_transport = models.CharField(max_length=1, choices=TRANSPORT_CHOICES, default=TRANSPORT_CHOICE_SHUTTLE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']