import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField("аватар", upload_to="images/avatars")

    class Meta(AbstractUser.Meta):
        pass

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # voters = models.ManyToManyField('User',verbose_name='голосовавшие', null=True, blank=True,related_name="voteds_post")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Voters(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voters = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.voters
