from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    git_hub_profile = models.URLField(max_length=300, null=True, blank=True, verbose_name='Профиль на GitHub')
    about = models.TextField(max_length=600, null=True, blank=True, verbose_name='О себе')

    def __str__(self):
        return self.user.first_name + "'s Profile"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        permissions = [
            ('can_view_all_users', 'может просматривать всех пользователей на одной странице')
        ]
