import datetime
from django.db import models


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date Published')

    def was_published_recently(self):
        return self.pub_date >= datetime.timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text  # 어떤 내용으로 보여질지 리턴해줌


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
