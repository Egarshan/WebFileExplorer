from django.db import models
import os

class File(models.Model):
	path = models.FileField(upload_to = '')


	def delete(self, *args, **kwargs):
		self.path.delete()
		super().delete(*args, **kwargs)

class Folder(models.Model):
	name = models.CharField(max_length = 100)


	def delete(self, *args, **kwargs):
		os.rmdir(os.path.dirname("media/") + '\\' + self.name)
		super().delete(*args, **kwargs)