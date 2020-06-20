from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    
    title = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=200, default="Inactive")
    created_by = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
    
    start_date = models.DateTimeField(null=True, blank=True)
    end_date= models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choices_set.all()

class Choices(models.Model):

    text     = models.TextField(blank=True, null=True)
    question = models.ForeignKey(Questions, null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question.title + '-' + self.text

    @property
    def answers(self):
        return self.answer_set.count()

class Answer(models.Model):

    user   =models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choices, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.user.first_name + '-' + self.choice.text
