from drivebundler.consts import PREF_CHOICE
from django.db import models
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import yaml

# Create your models here.
class Google(models.Model):
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def print_test():
        return PREF_CHOICE['TEST']

    def drive_write(title, text):
        gauth = GoogleAuth()
        gauth.CommandLineAuth()
        drive = GoogleDrive(gauth)

        f = drive.CreateFile({'title': title})
        f.SetContentString(text)
        f.Upload()
