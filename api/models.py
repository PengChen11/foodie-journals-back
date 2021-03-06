from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _


from django.conf import settings

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    ingredients = models.TextField(max_length=2500)
    steps = models.TextField(max_length=2500)
    meal_type = models.CharField(max_length=16)
    img_src_1 = models.URLField(blank=True, max_length=2500)
    img_src_2 = models.URLField(blank=True, max_length=2500)
    img_src_3 = models.URLField(blank=True, max_length=2500)
    difficulty = models.CharField(max_length=16, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
