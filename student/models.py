from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Students(models.Model):
    name = models.CharField('Name',max_length=200)
    roll_no = models.CharField('Roll Number',max_length=200,unique=True)
    dob =  models.DateField('Date Of Birth (yyyy-mm-dd)')

    def __str__(self):
        return self.name


class Marks(models.Model):
    idd = models.IntegerField(unique=True,primary_key=True)
    #idd = models.ForeignKey(Students,on_delete=models.CASCADE)
    mark = models.PositiveIntegerField('New Mark', null=True, validators=[MaxValueValidator(
        100), MinValueValidator(0)])

    def __str__(self):
        return str(self.idd)

    #class Meta:


