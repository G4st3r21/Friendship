from django.shortcuts import render
from .models import CollectedFriendshipsIRT


# Create your views here.

def response_stats(request):
    friendships = dict(
        (guild.guild_name, guild.friendships_count) for guild in CollectedFriendshipsIRT.objects.all()
    )

    context = {"friendships": friendships}

    return render(request, 'statistics/Stats.html', context=context)
