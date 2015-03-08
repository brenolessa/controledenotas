__author__ = 'MATHEUS'

from django import forms
from models import Disciplina

class FormDisciplina(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ("nome", "nota1", "nota2", "nota3")
        nota1 = forms.DecimalField(label="I unidade:")