from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Material(models.Model):
    # material_id = models.CharField(max_length=100,null=False)
    materialused = models.TextField(max_length=200,null=False)
    def __str__(self):
        return self.materialused

class Worked(models.Model):
    # work_id = models.CharField(max_length=100,null=False)
    worked = models.TextField(max_length=200,null=False)

    def __str__(self):
        return self.worked

class UsersAll(models.Model):
    # num_val = [(i,i) for i in range(1,)]

    image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    uname = models.CharField(max_length=50,null=False)
    work = models.ForeignKey(Worked,null=True,blank=True,on_delete=models.SET_NULL)
    material_used = models.ForeignKey(Material,on_delete=models.SET_NULL,null=True)
    cost = models.IntegerField(null=False)
    estimated_date = models.DateField()
    review = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.uname