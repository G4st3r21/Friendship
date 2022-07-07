from django.db import models


# Create your models here.

class CollectedFriendshipsIRT(models.Model):
    guild_name = models.CharField(max_length=15)
    friendships_count = models.IntegerField()
    color = models.CharField(max_length=10)
    cardholder_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.guild_name} = {self.friendships_count} дружбиков'


class CollectedFriendshipsBAT(models.Model):
    guild_name = models.CharField(max_length=15)
    count_1 = models.IntegerField()
    count_2 = models.IntegerField()
    count_3 = models.IntegerField()
    count_4 = models.IntegerField()
    count_5 = models.IntegerField()
    count_6 = models.IntegerField()
    count_7 = models.IntegerField()
    count_8 = models.IntegerField()
    count_9 = models.IntegerField()
    count_10 = models.IntegerField()
    count_11 = models.IntegerField()
    count_12 = models.IntegerField()
    count_13 = models.IntegerField()
    count_14 = models.IntegerField()
    count_15 = models.IntegerField()
    count_16 = models.IntegerField()
    count_17 = models.IntegerField()
    count_18 = models.IntegerField()

