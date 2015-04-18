from django.db import models
from django.contrib.auth.models import User
import random
import hashlib

class department(models.Model):
	code = models.CharField(max_length=6)
	name = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return self.code
	def save(self, force_insert=False, force_update=False):
		self.code = self.code.upper()
		super(department, self).save(force_insert, force_update)

class course(models.Model):
	department = models.ForeignKey(department)
	number = models.CharField(max_length=50)
	name = models.CharField(max_length=50, blank=True)
	description = models.TextField(blank=True)
	def __str__(self):
		return self.department.__str__() + self.number

class studygroup(models.Model):
	name = models.CharField(max_length=50)
	active = models.BooleanField(default=True)
	course = models.ManyToManyField(course)
	description = models.TextField(blank=True)
	owner = models.ForeignKey(User)
	groupid = models.CharField(max_length=10, unique=True, blank=True, editable=False)
	def __str__(self):
		return self.name
	def save(self, *args, **kwargs):
		randomid = hashlib.md5()
		if not self.groupid:
			# prevents guessing groupid
			randomid.update((self.name + str(random.randrange(100, 100000000))).encode('utf-8'))
			self.groupid = randomid.hexdigest()[0:10]
		success = False
		while not success:
			try:
				super(studygroup, self).save(*args, **kwargs)
			except IntegrityError:
				#try another random value
				randomid.update((self.name + str(random.randrange(100, 200000000))).encode('utf-8'))
				self.groupid = randomid.hexdigest()[5:25]
			else:
				success = True

class document(models.Model):
	course = models.ForeignKey(course)
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	document = models.FileField(upload_to='documents')
	owner = models.ForeignKey(User)
	def __str__(self):
		return self.name

class help_category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField(blank=True)
	priority = models.IntegerField(default=1)
	def __str__(self):
		return self.name

class help_question(models.Model):
	category = models.ForeignKey(help_category)
	question = models.TextField()
	answer = models.TextField()
	priority = models.IntegerField(default=1)
	def __str__(self):
		return self.question