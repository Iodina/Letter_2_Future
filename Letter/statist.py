from Letter.models import Letter
from django.utils import timezone


def num_send():
    return Letter.objects.all().count()

def num_delivered():
    l = Letter.objects.exclude(date_received__gt=timezone.now())
    return str(len(l))

def num_waiting():
    return str(len(Letter.objects.filter(date_received__gt=timezone.now())))

def num_pub():
    l = Letter.objects.filter(privacy=False).count()
    return str(l)

def num_priv():
    l = Letter.objects.filter(privacy=True).count()
    return str(l)

def date_first():
    list = [l.date_created for l in Letter.objects.all()]
    list.sort()
    return list[0]

def num_let_aday():
    first = date_first()
    num = ( timezone.now() - first).days
    if num:
        send = num_send()
        return str(send / num)[:5]
    else:
        return '0'

