from django.forms import ModelForm
from django import forms
from .models import Linguagem
from .models import Projeto
from .models import Cadeira

class PostForm(ModelForm):
    class Meta:
        model = Linguagem
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),

        }


help_texts = {

    'autor': 'Insira neste campo o nome do autor',
    'titulo': 'Insira neste campo o titulo',
    'descricao': 'Insira neste campo uma descricao',
    'link': 'Insira apenas um link'
}


labels ={
    'autor': 'Autor',
    'titulo': 'Titulo',
    'descricao': 'Descricao',
    'link': 'Link'

}
class ProjetoForm(ModelForm):
    class Meta:
        model = Projeto
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),

        }


help_texts = {

    'autor': 'Insira neste campo o nome do autor',
    'titulo': 'Insira neste campo o titulo',
    'descricao': 'Insira neste campo uma descricao',
    'link': 'Insira apenas um link'
}


labels ={
    'autor': 'Autor',
    'titulo': 'Titulo',
    'descricao': 'Descricao',
    'link': 'Link'

}
class CadeiraForm(ModelForm):
    class Meta:
        model = Cadeira
        fields = '__all__'

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'autor...'}),

        }


help_texts = {

    'autor': 'Insira neste campo o nome do autor',
    'titulo': 'Insira neste campo o titulo',
    'descricao': 'Insira neste campo uma descricao',
    'link': 'Insira apenas um link'
}


labels ={
    'autor': 'Autor',
    'titulo': 'Titulo',
    'descricao': 'Descricao',
    'link': 'Link'

}
