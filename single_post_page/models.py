from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=50, default='블로그 주인')
    bio = models.TextField(blank=True, help_text="간단한 자기소개를 입력하세요.")
    profile_image = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True,
        help_text="1:1 비율의 이미지를 권장합니다."
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "프로필"
        verbose_name_plural = "프로필"
