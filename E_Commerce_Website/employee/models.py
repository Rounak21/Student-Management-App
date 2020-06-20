from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary= models.IntegerField(null=True, blank=True)
    designation = models.CharField(max_length=100, null=False, blank=False)

    class Meta:

        ordering= ('-salary',)

    def __str__(self):

        return "{0} {1}".format(self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def user_changed(sender, instance, created, **kwargs):
    print(created)
    print(instance)
    
    if created:
        Profile.objects.create(user=instance)
    
    else:
        instance.profile.save()