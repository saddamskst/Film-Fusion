from django.db import models

class Contact_List(models.Model):
	
	Name=models.CharField(max_length=100)#, unique=True, blank=False)
	
	Email=models.CharField(max_length=200)
	Phone=models.IntegerField(max_length=200)
	Message=models.TextField(max_length=1200)
	
	class Meta:
		db_table='Contact_List'
		verbose_name = "Clients Word"
		
		
	def __str__(self):
		return self.Name