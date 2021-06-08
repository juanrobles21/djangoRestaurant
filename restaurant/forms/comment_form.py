from django import forms
from restaurant.models import Comment, QUALIFICATION_CHOICES


class CommentForm(forms.ModelForm):
    # opinion=forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}),required=False)
    # qualification=forms.ChoiceField(choices=QUALIFICATION_CHOICES, widget=forms.Select(), required=True)
    qualification = forms.ChoiceField(choices=QUALIFICATION_CHOICES, widget=forms.Select(), required=True)
    class Meta:
        model = Comment
        fields = [
                  'qualification',
                  'title_opinion',
                  'opinion'
                  ]
