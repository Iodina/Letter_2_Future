from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^$', views.letter, name='letter'),
    url(r'^statistics/$', views.statistics, name='statistics'),
    url(r'^public/$', views.public, name='public'),
    url(r'^write/$', views.write, name='write'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^public/(?P<letter_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^write/thanks/$', views.thanks, name='thanks'),
    url(r'^my_letters/$', views.my_letters, name='my_letters'),
    url(r'^my_letters/(?P<letter_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^contact/thanks/$', views.contact_thanks, name='contact_thanks'),

    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^register/$', views.register, name='register'),


]