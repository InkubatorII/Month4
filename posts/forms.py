from django import forms
from posts.models import Post


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if (title and content) and (title.lower() == content.lower()):
            raise forms.ValidationError('Заголовок и контент не должны совпадать')
        else:
            return cleaned_data

    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')

        if title and title.lower() == 'python':
            raise forms.ValidationError('Заголовок не может равняться слову Python')
        return title

class PostForm2(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'rate', 'image', 'tags']

