from django.db import models
from django.core.validators import RegexValidator

class Add_Movie(models.Model):
	
	Movie_Name=models.CharField(max_length=100)#, unique=True, blank=False)
	Movie_Image=models.ImageField(upload_to="Movie_Image")

	Year = models.CharField(
			max_length=4,
			validators=[
				RegexValidator(
					regex=r'^\d{4}$',
					message='Year must be a four-digit number.',
					code='invalid_year'
				)
			]
		)
	#Year=models.IntegerField(length=200)
	Genre=models.CharField(max_length=200)
	Description=models.TextField(max_length=1200)
	Cast_Name=models.CharField(max_length=1200)
	Directed_By=models.CharField(max_length=800)
	rating=models.DecimalField(max_digits=3,decimal_places=1)
    
	class Meta:
		db_table='Movie_List'
		verbose_name = "Add Movie"
        # verbose_name_plural = "Movie List"
	def __str__(self):
		return self.Movie_Name