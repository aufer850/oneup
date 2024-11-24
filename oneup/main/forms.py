from news.models import Comments
from django.forms import ModelForm

class commentform(ModelForm):
    class Meta:
        model = Comments
        fields = ['name','email','commenttext']