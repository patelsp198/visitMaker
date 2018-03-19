from django.db import models

# Create your models here.
class Reservation(models.Model):
	#organization name
	name = models.CharField(max_length=60)

	#organization email
	email = models.EmailField()

	#FIX_LATER, ->add min value
	people_number = models.IntegerField()

	TIME_CHOICES = (
		(9, '9:00am-10:00am'),
		(10, '10:00am-11:00am'),
		(11, '11:00am-12:00pm'),
		(12, '12:00pm-1:00pm'),
		(1, '1:00pm-2:00pm'),
		(2, '2:00pm-3:00pm'),
		(3, '3:00pm-4:00pm'),
	)
	#displays hour long intervals to choose from
	tour_time = models.IntegerField(
		choices=TIME_CHOICES
	)

	#syntax:
	# 	'yyyy-mm-dd'
	# 	'mm/dd/yyyy'
	# 	'mm/dd/yy'
	tour_date = models.DateField()

	#FIX_LATER, -> text field
	Special_Accomidations = models.TextField(blank=True)

	def __str__(self):
		return u'%s_%s' % (self.name, self.tour_date)