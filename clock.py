from apscheduler.schedulers.blocking import BlockingScheduler
from Letter.models import Letter
from django.contrib.auth.models import User

from django.core import mail
from django.utils import timezone

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    letter = [l for l in  Letter.objects.all() if l.date_received < timezone.now()]

    mails = [mail.EmailMessage(lett.subject,
                               lett.text,
                               User.objects.get(id=lett.author).email,
                                [lett.email],
                               ) for lett in letter
             ]
    connection = mail.get_connection()

    connection.open()
    connection.send_messages(mails)

    connection.close()
    return None


# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.start()