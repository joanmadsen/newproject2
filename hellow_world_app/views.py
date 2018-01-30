# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from hellow_world_app.models import Rock
from django.views.generic.list import ListView
from hellow_world_app.forms import CreateRockForm


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            'rock': Rock.objects.all().order_by('?'),
        }
        return context

    def get_template_names(self):
        return ["rock_list.html"]


class RockDetail(TemplateView):
    template_name = 'rocks/rock_detail.html'

    def get(self, request, *args, **kwargs):
        context = {
            'rock': Rock.objects.get(id=kwargs['id'])
        }
        return self.render_to_response(context)


class CreateRock(CreateView):
    template_name = 'rocks/CreateRock.html'
    model = Rock
    fields = ['name', 'description', 'slug']

