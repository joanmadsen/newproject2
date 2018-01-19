# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from hellow_world_app.models import Rock
from django.views.generic.list import ListView


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
       context = {
           'number': 6,
            'rock': Rock.objects.all().order_by('?'),

       }
       return self.render_to_response(context)

class RockList(ListView):
    model = Rock
