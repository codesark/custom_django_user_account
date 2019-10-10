from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuth(object):
  def authenticate(self, request, username=None, password=None):
    try:
      user = User.objects.get(username=username)
      if user.check_password(password):
        return user
    except User.DoesNotExist:
      try:
        user = User.objects.get(email=username)
        if user.check_password(password):
          return user
      except User.DoesNotExist:
        try:
          user = User.objects.get(phone_number=username)
          if user.check_password(password):
            return user
        except:
          return None
        return None
      return None
  

  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None