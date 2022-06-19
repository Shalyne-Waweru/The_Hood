from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    description = models.TextField()
    emergency_number = models.IntegerField()
    police_number = models.IntegerField()
    hood_image = models.ImageField(upload_to='hood-images/')
    occupants = models.ForeignKey(User,on_delete=models.CASCADE, related_name='occupants',null=True, default=0)

    def __str__(self):
        return {self.name}

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()


class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
  bio = models.TextField(max_length=500, default="My Bio", blank=True)
  profile_pic = models.ImageField(upload_to='profile-images/', default='default.png')
  location = models.CharField(max_length=50, default="My Location", blank=True)
  neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='hood', default=0)

  def __str__(self):
        return f'{self.user.username} Profile Details'

  #Create a profile for every signed in user
  # @receiver(post_save, sender=User)
  # def update_user_profile(sender, instance, created, **kwargs):
  #     if created:
  #         Profile.objects.create(user=instance)
  #     instance.profile.save()

  def save_profile(self):
    self.save()

  def del_profile(self):
    self.delete()


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    business_image = models.ImageField(upload_to='business-images/', default='default.png')
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, related_name='neighbourhood')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return {self.name}

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term).all()
        return businesses