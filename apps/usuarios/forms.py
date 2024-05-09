from typing import Any, Mapping
from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList
class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Usuário',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: João Silva'
            }
        )
    )
    
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )
class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label='Nome completo',
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: João Silva'
            }
        )
    )
    email=forms.EmailField(
        label='E-mail',
        required=True,
        max_length=150,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex: Joao@email.com'
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite sua senha'
            }
        )
    )
    confirma_senha=forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirme sua senha'
            }
        )
    )
    def clean_nome_cadastro(self):
        data = self.cleaned_data.get("nome_cadastro")
        if data:
            data = data.strip()
            if ' ' in data :
                raise forms.ValidationError('não é possivel ter espaços')
            else:
                return data
    
    def clean_confirma_senha(self):
        confirma = self.cleaned_data.get("confirma_senha")
        senha = self.cleaned_data.get('senha')
        if senha and confirma:
            if senha!=confirma:
                raise forms.ValidationError('as senha não são iguais')
            else:
                return senha
    
