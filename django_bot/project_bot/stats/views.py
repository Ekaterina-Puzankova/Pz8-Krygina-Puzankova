

# Create your views here.
from django.shortcuts import render
from django.db.models import Count
from .models import Message
from django.utils import timezone
from datetime import timedelta


def statistics_view(request):
    today = timezone.now().date()
    yesterday = today - timedelta(days=1)

    daily_stats = Message.objects.filter(date__date=today).count()
    yesterday_stats = Message.objects.filter(date__date=yesterday).count()

    user_stats = Message.objects.values('username').annotate(message_count=Count('username')).order_by('-message_count')
    command_stats = Message.objects.values('command').annotate(command_count=Count('command')).order_by('-command_count')

    context = {
        'daily_stats': daily_stats,
        'yesterday_stats': yesterday_stats,
        'user_stats': user_stats,
        'command_stats': command_stats
    }
    return render(request, 'stats/statistics.html', context)

def index(request):
    return render(request, 'stats/index.html')