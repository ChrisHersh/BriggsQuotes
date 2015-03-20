from django.db import models

class BriggsQuote(models.Model):
	quote_text = models.CharField(max_length=256)
	votesPos = models.IntegerField(default=0)
	votesNeg = models.IntegerField(default=0)
#	pkey = models.AutoField()
	visible = models.BooleanField(default=True)

	def __str__(self):
		return self.quote_text


class BriggsVote(models.Model):
	quote = models.ForeignKey(BriggsQuote)
	ip = models.GenericIPAddressField()

	def __str__(self):
		return self.quote

