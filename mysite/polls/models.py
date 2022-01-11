from django.db import models


class Question(models.Model):
    question_text = models.CharField('问题', max_length=200)
    pub_date = models.DateTimeField('创建时间')
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('选择', max_length=200)
    votes = models.IntegerField('票数', default=0)
    
    def __str__(self):
        return  self.choice_text