from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.
class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta: 
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.my_field_name

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a Articles genre (e.g. Finance)')
    #id=models.AutoField(primary_key=True)	
    class Meta:
        db_table = "Genre"
		
class User(models.Model):
	First_name = models.CharField(max_length=200, help_text='Enter your First Name ')
	Last_name = models.CharField(max_length=200, help_text='Enter your Last Name ')
	email = models.CharField(max_length=200, help_text='Enter your email ')
	area = models.CharField(max_length=200, help_text='Enter your area ')
	#id = models.AutoField(primary_key=True)
	class Meta:
		db_table = "User"
	

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    #id=models.AutoField(primary_key=True)	
    username=models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    job = models.CharField(max_length=100)
    class Meta:
	    db_table = "Author"
	

class Articles(models.Model):
	title = models.CharField(max_length=200)
	url   = models.CharField(max_length=200)
	genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True,db_constraint=False)
	date_published = models.DateField(null=True, blank=True)
	#id=models.AutoField(primary_key=True)	
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	class Meta:
		db_table = "Articles"

class Area(models.Model):
	#id	=models.AutoField(primary_key=True)	
	Name=models.CharField(primary_key=True,max_length=100)
	color=models.CharField(max_length=100)
	img_id=models.CharField(max_length=100)
	total_cases=models.IntegerField(default=0)
	total_deaths=models.IntegerField(default=0)
	total_recovers=models.IntegerField(default=0)
	total_hospitals=models.IntegerField(default=0)
	population=models.IntegerField(default=0)
	class Meta:
	    db_table = "Area"
	
	

class Hospital(models.Model):
	#id =models.AutoField(primary_key=True)	
	area_id=models.ForeignKey(Area, on_delete=models.CASCADE,db_constraint=False)
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	class Meta:
	    db_table = "Hospital"
	
	
class Cases(models.Model):	
		
	area_id=models.ForeignKey(Area, on_delete=models.CASCADE,db_constraint=False)
	dead = models.BooleanField(default=False)
	recovered= models.BooleanField(default=False)
	on_going=models.BooleanField(default=True)
	
	
	class Meta:
	    db_table = "Cases"

	
class SuperMarket(models.Model):
	#id =models.AutoField(primary_key=True)	
	area_id=models.ForeignKey(Area, on_delete=models.CASCADE,db_constraint=False)
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	class Meta:
	    db_table = "SuperMarket"
	
class Pharmacies(models.Model):
	#id =models.AutoField(primary_key=True)	
	area_id=models.ForeignKey(Area, on_delete=models.CASCADE,db_constraint=False)
	name=models.CharField(max_length=100)
	location=models.CharField(max_length=100)
	class Meta:
	    db_table = "Pharmacies"
    	

class Diagramms(models.Model):
	#id =models.AutoField(primary_key=True)
	img=models.CharField(max_length=100)
	area_id=models.ForeignKey(Area, on_delete=models.CASCADE,db_constraint=False)
	description=models.CharField(max_length=100)
	class Meta:
	    db_table = "Diagramms"


class Tweets(models.Model):
	#id =models.AutoField(primary_key=True)
	img=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	class Meta:
	    db_table = "Tweets"


