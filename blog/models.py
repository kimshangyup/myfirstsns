from django.db import models

# Create your models here.



class Category(models.Model):
	title=models.CharField(max_length=20,null=False)


class Entries(models.Model):
	title=models.CharField(max_length=40,null=False, unique=True)
	text=models.TextField(null=False)
	Comment=models.IntegerField(default=0,null=True)
	category=models.ForeignKey(Category)
	created=models.DateTimeField(auto_now=True)

class Comment(models.Model):
	name=models.CharField(max_length=20,null=False)
	password=models.CharField(max_length=20,null=False)
	text=models.CharField(max_length=50,null=False)
	created=models.DateTimeField(auto_now=True)
	entry=models.ForeignKey(Entries)
