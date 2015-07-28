from django.http import HttpResponse
from Letter.models import Letter
from django.template import Context
from django.template.loader import get_template


def hello(request):
    return HttpResponse("It's a welcome page")

