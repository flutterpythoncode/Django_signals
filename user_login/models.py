from django.db import models
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver


class userData(models.Model):

    fullname=models.CharField(max_length=100,null=True)
    age=models.IntegerField(null=True)
    userid=models.CharField(max_length=100, null=True)
    
@receiver(post_save, sender=userData)
def test_post_save(sender, instance, created, **kwargs):
    # print(f'{(instance.fullname)}-{str(instance.id).zfill(5)}')
    if created:
        instance.userid=f'{(instance.fullname)}-{str(instance.id).zfill(5)}'
        instance.save()

@receiver(pre_save, sender=userData)    
def test_pre_save(sender, instance, **kwargs):
    print("pre save called")

@receiver(post_delete, sender=userData)
def deleteRecord(sender, instance, **kwargs):
    userId=instance.userid
    print("Deleted user id: "+userId)
    

