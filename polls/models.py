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
    description = models.TextField("Описание вопроса")
    pub_date = models.DateTimeField('date published',default=datetime.datetime.now())
    votes = models.IntegerField(default=0)
    pic = models.ImageField("картинка поста", upload_to="images/pics", null=True, blank=True)
    num_of_questions = models.IntegerField(null=False, default=3)


    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    def procent(self):
        return round(100 * self.votes / self.question.votes)

    def __str__(self):
        return self.choice_text

class Voters(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    voter = models.ForeignKey('User', on_delete=models.CASCADE)
    choise = models.ForeignKey('Choice',on_delete=models.CASCADE)

    def __str__(self):
        return self.voter.username +" " + self.question.question_text
