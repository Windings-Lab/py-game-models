from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="skills",
    )


class Guild(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)


class Player(models.Model):
    nickname = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    bio = models.CharField(max_length=255)
    race = models.ForeignKey(
        Race,
        on_delete=models.CASCADE,
        related_name="races",
    )
    guild = models.ForeignKey(
        Guild,
        on_delete=models.SET_NULL,
        null=True,
        related_name="guilds"
    )
    created_at = models.DateTimeField(auto_now_add=True)
