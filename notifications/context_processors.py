from .models import Notification

def notification_count(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
        notification_count = notifications.count()
    else:
        notification_count = 0

    return {
        'notification_count': notification_count
    }