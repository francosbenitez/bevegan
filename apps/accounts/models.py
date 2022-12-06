from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from config.settings import MEDIA_URL, STATIC_URL
# Create your models here.

class UserManager(BaseUserManager):
   
    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
			
        user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

        user.set_password(password)
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True, verbose_name='username')
    name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.IntegerField(verbose_name='phone')
    # image = models.ImageField(upload_to='accounts/%Y/%m/%d', null=True, blank=True)
    # birthdate = models.DateField(verbose_name='birthdate')

    objects = UserManager() 
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username']


    # class Meta: 
    #     verbose_name = ('user')
    #     verbose_name_plural = ('users')

    def __str__(self):
        return self.username
        
    def get_full_name(self):
        return f'{self.name} {self.last_name}'  

    def get_short_name(self):
        return self.name

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'accounts/user_default.png')

    def __str__(self) -> str:
        return f'{self.name} {self.email}'