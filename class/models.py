from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class Status(models.IntegerChoices):
    INACTIVE = 0, "INACTIVE"
    ACTIVE = 1, "ACTIVE"
    OTHER = 2, "OTHER"


# class School(models.Model):
#     number = models.IntegerField()    
#     name = models.CharField(max_length=300, default='maktab')
#     location = models.CharField(max_length=300, blank=True)
#     ca = models.DateTimeField(auto_now_add=True, verbose_name='yaratildi')
#     ua = models.DateTimeField(auto_now=True, verbose_name="o'zgartirildi")
#     status = models.PositiveSmallIntegerField(
#         choices=Status.choices,
#         default=Status.ACTIVE
#     )
#     def __str__(self):
#         return str(self.number) + ' - ' + self.name


class Sinf(models.Model):
    # school = models.ForeignKey("School", on_delete=models.CASCADE, default=School.objects.latest(), related_name='school') # 'id'
    number = models.IntegerField()
    room = models.CharField(max_length=300, default='hona')
    ca = models.DateTimeField(auto_now_add=True, verbose_name='yaratildi')
    ua = models.DateTimeField(auto_now=True, verbose_name="o'zgartirildi")
    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.ACTIVE
    )
    def __str__(self):
        return str(self.number) + ' - ' + self.name


class Position(models.Model):  # lavozim: o'qituvchi, o'quvchi, direktor, ota-ona, oddiy odam
    name = models.CharField(max_length=200, unique=True,
                            verbose_name="lavozim")
    ca = models.DateTimeField(auto_now_add=True, verbose_name='yaratildi')
    ua = models.DateTimeField(auto_now=True, verbose_name="o'zgartirildi")
    
    def __str__(self):
        return self.name


class Profile(AbstractBaseUser):
    username = models.CharField(max_length=300, verbose_name="login")
    first_name = models.CharField(max_length=200, verbose_name="ism")
    last_name = models.CharField(max_length=200, verbose_name="familiya")
    middle_name = models.CharField(max_length=200, verbose_name="otasining ismi")
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True, default=None)
    phone = models.CharField(max_length=200, null=True, verbose_name="telefon")
    email = models.EmailField(max_length=200, null=True, verbose_name="e-pochta")
    profile_pic = models.ImageField(upload_to=get_file_path, null=True, blank=True, default='profile_pic/profile.jpg', verbose_name="rasm")
    directory_string_var = 'profile_pic'
    ca = models.DateTimeField(auto_now_add=True, verbose_name='yaratildi')
    ua = models.DateTimeField(auto_now=True, verbose_name="o'zgartirildi")
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.ACTIVE, verbose_name="holat")


    objects = ProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


    class Meta:
        ordering = ["id"]
        # verbose_name_plural = "3.Profiles"






















