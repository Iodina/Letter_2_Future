#!/usr/bin/env python
from Letter.models import Letter

from django.core import mail
from django.utils import timezone





def cronjob():

    letter = [l for l in  Letter.objects.all() if l.date_received > timezone.now()]

    mails = [mail.EmailMessage(lett.subject,
                               lett.text,
                               'mariya.metelitsa@gmail.com',
                                [lett.email],
                               ) for lett in letter
             ]
    connection = mail.get_connection()

    connection.open()
    connection.send_messages(mails)

    connection.close()
    return None


# cronjob()

