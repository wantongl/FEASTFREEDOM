from django.db import models

# Create your models here.
class Kitchen2Register(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    email=models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchens/', blank=True)
    description = models.TextField(blank=True)
    TIMES_TO_WORK = [
        ('Tm1','8:00'),
        ('Tm2','8:30'),
        ('Tm3','9:00'),
        ('Tm4','9:30'),
        ('Tm5','10:00'),
        ('Tm6', '10:30'),
        ('Tm7', '11:00'),
        ('Tm8', '11:30'),
        ('Tm9', '12:00'),
        ('Tm10', '12:30'),
        ('Tm11', '13:00'),
        ('Tm12', '13:30'),
        ('Tm13', '14:00'),
        ('Tm14', '14:30'),
        ('Tm15', '15:00'),
        ('Tm16', '15:30'),
        ('Tm17', '16:00'),
        ('Tm18', '16:30'),
        ('Tm19', '17:00'),
    ]
    startTime=models.CharField(max_length=4,choices=TIMES_TO_WORK,default='Tm1',)
    endTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    monday=models.BooleanField(default=False)
    tuesday=models.BooleanField(default=False)
    wednesday = models.BooleanField(default=False)
    thursday = models.BooleanField(default=False)
    friday = models.BooleanField(default=False)
    saturday = models.BooleanField(default=False)
    sunday = models.BooleanField(default=False)
