from django import forms
from django.db.models.expressions import Value
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choices_list = []

for item in choices:
    choices_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets ={

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agregar el titulo al blog!'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Agregar el tema referido'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
           'author': forms.TextInput(attrs={'class': 'form-control','value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Desarrollo del tema'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets ={

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'acá va algo de titulo!!! :)'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),

            }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets ={

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
            }