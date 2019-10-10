import random
import string

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from core.utils import avatar_upload_location, randomString

# ------------------ CLASSES ---------------------------

# Custom User Manager Class
class UserManager(BaseUserManager):

  def _create_user(self, first_name, last_name, password, is_staff, is_superuser, username=None, email=None, phone_number=None, **kwargs):

    now = timezone.now()

    if not first_name:
      raise ValueError("You must enter a first name")

    if not last_name:
      raise ValueError("You must enter a last name")

    if not password:
      raise ValueError("You must enter a password")

    # Creates an username from email if doesn't exists
    if username is None:
      fname = str(self.cleaned_data['first_name']).lower().replace(' ', '')
      lname = str(self.cleaned_data['last_name']).lower().replace(' ', '')
      username = ''.join([fname, lname, randomString()])

    print('Your username is ', username)

    email = self.normalize_email(email)

    user = self.model(username = username,
                      first_name=first_name,
                      last_name=last_name,
                      is_staff = is_staff,
                      is_active = True,
                      is_superuser = is_superuser,
                      last_login = now,
                      date_joined = now,

                      email = email,
                      phone_number = phone_number,

                      **kwargs)

    user.set_password(password)
    user.save(using=self.db) 
    
    return user

  # Creates a normal user
  def create_user(self, first_name, last_name, username=None, email=None, phone_number=None, password=None, **kwargs):
    return self._create_user(first_name, last_name, password, False, False, username, email, phone_number, **kwargs)

  # Creates a superuser
  def create_superuser(self, first_name, last_name, username=None, email=None, phone_number=None, password=None, **kwargs):
    return self._create_user(first_name, last_name, password, True, True, username, email, phone_number, **kwargs)


# Custom User Model Class
class User(AbstractBaseUser, PermissionsMixin):
  
  first_name = models.CharField(max_length=240)
  last_name = models.CharField(max_length=240)

  username = models.CharField(max_length=254, unique=True)
  
  email = models.EmailField(blank=True, null=True)
  phone_number = PhoneNumberField(blank=True, null=True)

  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  is_active = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True)

  GENDER_CHOICES = (
    ('ML', 'Male'),
    ('FL', 'Female'),
    ('TS', 'Transgender'),
    ('OT', 'Other'),
  )
  age = models.PositiveSmallIntegerField(blank=True, null=True)
  gender = models.CharField(max_length=5, choices=GENDER_CHOICES, blank=True, null=True)

  avatar = models.ImageField(blank=True, null=True, upload_to=avatar_upload_location)
  bio = models.CharField(max_length=512, blank=True, null=True)
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['first_name', 'last_name']
  EMAIL_FIELD = 'email'

  objects = UserManager()

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')
  
  def __str__(self):
    return self.username

  def get_full_name(self):
    if self.first_name != '':
      return '%s %s' %(self.first_name, self.last_name)
    else:
      return self.username

  def get_short_name(self):
    return '%s' %(self.first_name)
      
  def get_absolute_url(self):
    pass

  def email_user(self, subject, message, from_email=None, **kwargs):
    send_mail(subject, message, from_email, [self.email], **kwargs)
