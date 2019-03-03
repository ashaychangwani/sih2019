from django.forms import ModelForm, DateInput
from .models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),#change format
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'), #
    }
    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)# remove %H%M
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)#
