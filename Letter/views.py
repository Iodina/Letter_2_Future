from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from Letter.models import Letter
from django.template import Context, RequestContext, loader
from django.template.loader import get_template
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.context_processors import csrf
import datetime
from Letter.forms import ContactForm, LetterForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  UserCreationForm
from django.conf import settings
from Letter.statist import *
import sendgrid

def contact(request):


    sg = sendgrid.SendGridClient('app39439144@heroku.com', 'rv5ufdwq5977')



    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = sendgrid.Mail()
            message.add_to('mariya.metelitsa@gmail.com')
            message.set_subject(cd['subject'])
            message.set_text(cd['message'])
            message.set_from(cd.get('email', ''))
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email', ''),
            #     ['mariya.metelitsa@gmail.com'],
            # )
            status, msg = sg.send(message)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site!',
                     'email': 'vasya.pupkin@gmail.com',
                     'message':'Hi, guys! Your web-site is great!'
                     }
        )

    return render(request, 'Letter/contact.html', {'form': form, 'nbar':'contact',})

def letter(request):
    t = get_template('Letter/welcome.html')
    result = t.render(Context({'user':request.user, 'nbar':'home',}))
    return HttpResponse(result)

def my_letters(request):
    my_letters_list = Letter.objects.filter(author=request.user).order_by('-date_created')
    template = loader.get_template('Letter/my_letter.html')
    context = RequestContext(request, {
        'my_letters_list': my_letters_list,'nbar':'my_letters',
    })
    return HttpResponse(template.render(context))

def public(request,):
    latest_letters_list = Letter.objects.filter(privacy=False).order_by('-date_created')[:20]
    template = loader.get_template('Letter/public.html')
    context = RequestContext(request, {
        'latest_letters_list': latest_letters_list,'nbar':'public',
    })
    return HttpResponse(template.render(context))

def detail(request, letter_id):
    l = Letter.objects.get(id=letter_id)
    f = LetterForm(instance=l)
    return render_to_response('Letter/detail.html', {'letter_number': letter_id,'form':f,  }, context_instance=RequestContext(request))



@login_required
def write(request):
    mdict = {}
    if request.method == 'POST':
        form = LetterForm(request.POST)
        mdict.update(csrf(request))
        if form.is_valid():
            cd = form.cleaned_data
            l = Letter(
                recipient=cd['recipient'],
                subject=cd['subject'],
                email=cd.get('email', 'noreply@example.com'),
                text=cd['text'],
                date_created=datetime.datetime.now(),
                date_received=cd['date_received'],
                privacy=cd['privacy'],
                author=request.user
            )
            l.save()
            return HttpResponseRedirect('/write/thanks/')
    else:
        form = LetterForm(
            initial={ 'recipient':'Vasya Pupkin',
                      'email':'vasya@gmail.com',
                      'subject':'Happy B-day!',
                      'text':"You're 80, grandpa! ;)"}
        )
    mdict.update(csrf(request))
    mdict = RequestContext(request, {'form':form , 'nbar':'write',})
    return render_to_response('Letter/write.html', mdict)



def statistics(request):
    t = get_template('Letter/statistics.html')

    result = t.render(Context({'user':request.user,
                               'num_send': num_send(),
                               'num_delivered': num_delivered(),
                               'num_waiting': num_waiting(),
                               'num_pub': num_pub(),
                               'num_priv': num_priv(),
                               'date_first':str(date_first())[:str(date_first()).find('.')],
                               'num_let_aday':num_let_aday(),
                               'nbar':'statistics',
                               }
                              )
                      )
    return HttpResponse(result)

def thanks(request):
    t = get_template('Letter/write.thanks.html')
    result = t.render(Context({'user':request.user}))
    return HttpResponse(result)

def contact_thanks(request):
    t = get_template('Letter/contact.thanks.html')
    result = t.render(Context({'user':request.user}))
    return HttpResponse(result)

def faq(request):
    t = get_template('Letter/FAQ.html')
    result = t.render(Context({'user':request.user, 'nbar':'faq',}))
    return HttpResponse(result)
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')
    args = {}
    args.update(csrf(request))
    args['user_form']=UserForm()
    return render_to_response('Letter/register.html',args)


def register_success(request):
    return render_to_response('Letter/register_success.html')