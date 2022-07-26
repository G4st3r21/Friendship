from django.shortcuts import render
from .models import CollectedFriendshipsIRT, CollectedFriendshipsBAT
from datetime import date


# Create your views here.

def response_stats(request):
    friendships_count = dict(
        (guild.guild_name,
         [
             guild.color,
             guild.friendships_count,
             guild.cardholder_name,
             pos
         ])
        for pos, guild in enumerate(CollectedFriendshipsIRT.objects.all().order_by("friendships_count").reverse())
    )

    # print(type(CollectedFriendshipsBAT.objects.all()))
    # for guild in CollectedFriendshipsBAT.objects.all():
    #     print(type(guild))

    today = date.today().strftime("%d.%m.%Y")

    context = {
        "friendships": friendships_count,
        "today": today
    }

    return render(request, 'statistics/Stats.html', context=context)
