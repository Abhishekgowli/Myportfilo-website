from django.db import models

# Create your models here.
class ProjectData(models.Model):
    pname=models.CharField(max_length=500)
    techUsed=models.CharField( max_length=200)
    pmonth=models.CharField(max_length=50)
    pyear=models.IntegerField()
    pdescrpation=models.TextField()
    plink=models.CharField(max_length=500)
    created_date=models.DateField(auto_now_add=True)
