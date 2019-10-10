import random
import string
from django.utils.timezone import timezone


#  ----------------- FUNCTIONS ----------------------

# Function to generate random string of number having random
def randomString():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(int(random.choice(string.digits))))


# Function to define avatar upload location
def avatar_upload_location(instance, filename):
  return "user/avatar/%s/%s/%s" % (instance.id, str(timezone.now().strftime("%Y/%m")), filename)
