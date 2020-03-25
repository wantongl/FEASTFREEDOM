from django.db import models
from django.urls import reverse
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class menuItem(models.Model):
    name=models.CharField(max_length=200,db_index=True,default='')
    veg=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=10, decimal_places=2,db_index=True,default='')

    def __str__(self):
        return self.name

class Kitchen2Register(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200, db_index=True)
    email=models.CharField(max_length=50)
    image = models.ImageField(upload_to='kitchens/',blank=True)
    description = models.TextField(blank=True)
    #menu=models.ForeignKey(menuItem,on_delete=models.CASCADE,blank=True,null=True)
    menu = models.ManyToManyField(menuItem)
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
    monday = models.BooleanField(default=False)
    mondayStartTime = models.CharField(max_length=4,choices=TIMES_TO_WORK,default='Tm1',)
    mondayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    tuesday=models.BooleanField(default=False)
    tuesdayStartTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm1', )
    tuesdayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    wednesday = models.BooleanField(default=False)
    wednesdayStartTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm1', )
    wednesdayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    thursday = models.BooleanField(default=False)
    thursdayStartTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm1', )
    thursdayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    friday = models.BooleanField(default=False)
    fridayStartTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm1', )
    fridayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    saturday = models.BooleanField(default=False)
    saturdayStartTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm1', )
    saturdayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )
    sunday = models.BooleanField(default=False)
    sundayStartTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm1', )
    sundayEndTime = models.CharField(max_length=4, choices=TIMES_TO_WORK, default='Tm19', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('userModule:kitchen_detail', args=[self.id])
