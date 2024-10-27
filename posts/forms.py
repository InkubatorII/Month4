from django import forms
from posts.models import Post, Tag, Comment


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
    rate = forms.IntegerField()

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

    widgets = {
        'content': forms.Textarea(
            attrs={
                'placeholder': 'Введите текст',
                'rows': 5,
                'cols': 30,
                'class': 'form-control',

            }
        )
    }
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

class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите текст для поиска',
                'class': 'form-control',
            }
        )
    )
    tags = forms.ModelMultipleChoiceField(
        required=False, queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    orderings = (
        ('title', 'По названию'),
        ('-title', 'По названию в обратно порядке'),
        ('rate', 'По рейтингу'),
        ('-rate', 'По рейтингу в обратно порядке'),
        ('created_at', 'По дате создания'),
        ('-created_at', 'По дате создания в обратном порядке'),
    )

    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

class CommentForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Введите текст',
                'rows': 5,
                'cols': 30,
                'class': 'form-control',
            }
        )
    )