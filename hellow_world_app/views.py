# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
       context = {
           'number': 6,
       }
       return self.render_to_response(context)

