from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


#........ Domain Models .......

class Author(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

  class Meta:
    permissions = [
      ("can_add_book", "can add book"),
      ("can_change_book", "can change book"),
      ("can_delete_book", "can delete book"),
    ]

  def __str__(self):
    return self.title

class Library(models.Model):
  name = models.CharField(max_length=100)
  books = models.ManyToManyField(Book, related_name='libraries')

  def __str__(self):
    return self.name

class Librarian(models.Model):
  name = models.CharField(max_length=100) 
  library = models.OneToOneField(Library, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  

#...........Custom User ............

class CustomUserManager(BaseUserManager):
  def create_user(self, username, password=None, **extra_fields):
    if not username:
      raise ValueError("The username must be set")
    
    user = self.model(username=username, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, username, password=None, **extra_fields):
    extra_fields.setdefault("is_staff", True)
    extra_fields.setdefault("is_superuser", True)

    return self.create_user(username, password, **extra_fields)
  


class CustomUser(AbstractUser)  :
  date_of_birth = models.DateField(null=True, blank=True)
  profile_photo = models.ImageField(upload_to='profiles/', null=True, blank=True)

  objects = CustomUserManager()

  def __str__ (self):
    return self.username   
  

#............... UserProfile ...........

class UserProfile(models.Model):
  ROLE_CHOICES = (
    ('Admin', 'Admin'),
    ('Librarian', 'Librarian'),
    ('Member', 'Member'),
  )  

  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

  def __str__(self):
    return f"{self.user.username} - {self.role}"
  
#Automatic profile creation
@receiver(post_save, sender=CustomUser)  
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)

