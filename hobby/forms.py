from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.TextInput(attrs={'autofocus': 'autofocus',
                                                  'placeholder': 'New Topic Name',
                                                  })}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['topic', 'text', ]
        labels = {'topic': 'Select Topic',
                  'text': 'Your Entry',
                  }
        widgets = {'text': forms.Textarea(
            attrs={'cols': 80,
                   'placeholder': 'Enter your entry information here ...',
                   'autofocus': 'autofocus'})}
