import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Items(models.Model):
	item_id=models.CharField(max_length=10,primary_key=True)
	name=models.CharField(max_length=30)
	unit=models.CharField(max_length=10)
	quantity=models.IntegerField(default=0)
	balance=models.IntegerField(default=0)
	timestamp=models.DateTimeField('date recently modified')

	def __unicode__(self): 
		return u'%s' % (self.item_id)


class Units(models.Model):
	name=models.OneToOneField(Items)
	shorthand=models.CharField(max_length=10)

	def __unicode__(self):
		return u'%s %s' % (self.name,self.shorthand)


class Transactions(models.Model):
	item=models.ForeignKey(Items)
	transaction_type=models.CharField(max_length=10)
	quantity=models.IntegerField(default=0)
	cost=models.IntegerField(default=0)
	inventory=models.IntegerField(default=0)
	date=models.DateTimeField('Date issued')
	timestamp=models.DateTimeField('Transaction date')
	consumption=models.IntegerField(default=0)
	comments=models.CharField(max_length=50)

	def was_transacted_recently(self):
		return self.timestamp >= timezone.now() - datetime.timedelta(days=1)
	was_transacted_recently.admin_order_field = 'timestamp'
	was_transacted_recently.boolean = True
	was_transacted_recently.short_description = 'transacted recently?'

	def __unicode__(self):
		return u'%s %s' % (self.item,self.date)
