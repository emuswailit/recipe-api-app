from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin



class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **extra_fields):
        """Create new user using email, name"""
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):

    """Customizes user model that supports use of
    email to create user and not username"""
    email= models.EmailField(max_length= 255, unique=True)
    name= models.CharField(max_length= 255)
    is_active= models.BooleanField(default= True)
    is_staff= models.BooleanField(default= False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]
