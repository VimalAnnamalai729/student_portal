from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Adding your custom fields
    user_id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    email = models.EmailField(unique=True, blank=False)  # Email as a unique field
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female')],
        blank=False
    )
    yrs_of_exp = models.FloatField(null=True, blank=False)
    coding_exp_in_yrs = models.FloatField(null=True, blank=False)
    batch_no = models.CharField(max_length=50, blank=False)

    # Automatically inherited fields from AbstractUser:
    # username, first_name, last_name, password, email, is_staff, is_active,
    # is_superuser, last_login, date_joined

    # # Update required fields for superuser creation
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Use email as the username field
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
