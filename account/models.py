from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password1, password2):
        if len(password1) < 8:
            raise ValueError

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password1)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)

        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    idx = models.AutoField(primary_key=True)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=32)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All superusers are staff
        return self.is_superuser
