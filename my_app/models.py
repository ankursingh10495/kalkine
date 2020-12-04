from django.db import models

# Create your models here.
class CardDetail(models.Model):
	card_title = models.CharField(max_length=100, null=True)
	card_text = models.CharField(max_length=100, null=True)

	def __str__(self):
		self.card_title

	class Meta:
		db_table = 'card_detail'
