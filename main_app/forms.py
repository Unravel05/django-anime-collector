from django.forms import ModelForm
from .models import Phasing

class PhasingForm(ModelForm):
  class Meta:
    model = Phasing
    fields = ['date', 'status']