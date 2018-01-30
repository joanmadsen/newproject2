from django.forms import ModelForm
from hellow_world_app.models import Rock



class CreateRockForm(ModelForm):
    class Meta:
        model = Rock
        field = ['name', 'description']
        exclude = []

form = CreateRockForm()
