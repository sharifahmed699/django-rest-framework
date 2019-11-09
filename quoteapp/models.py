from django.db import models

# Create your models here.
class QuoteCategory(models.Model):
	title = models.CharField(max_length = 50)

	def __str__(self):
		return self.title


class Quote(models.Model):
	Quote = models.TextField()
	author = models.CharField(max_length = 100)

	quote_category = models.ForeignKey( 
		'QuoteCategory',
		 on_delete = models.CASCADE
	)

		