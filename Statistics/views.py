from django.shortcuts import render
from .models import CollectedFriendshipsIRT
from datetime import date


# Create your views here.

def response_stats(request):
    friendships_count = dict(
        (guild.guild_name,
         [
             guild.color,
             guild.friendships_count,
             guild.cardholder_name
         ])
        for guild in CollectedFriendshipsIRT.objects.all()
    )

    today = date.today().strftime("%d.%m.%Y")

    context = {
        "friendships": friendships_count,
        "today": today
    }

    return render(request, 'statistics/Stats.html', context=context)
