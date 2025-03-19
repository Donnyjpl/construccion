from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje', 'tipo_proyecto', 'presupuesto']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu nombre')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Tu correo electrónico')}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Tu número de teléfono')}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Asunto')}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': _('Tu mensaje')}),
            'tipo_proyecto': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', _('-- Seleccionar tipo de proyecto --')),
                ('residencial', _('Residencial')),
                ('comercial', _('Comercial')),
                ('industrial', _('Industrial')),
                ('renovacion', _('Renovación')),
                ('otro', _('Otro')),
            ]),
            'presupuesto': forms.Select(attrs={'class': 'form-control'}, choices=[
                ('', _('-- Seleccionar rango de presupuesto --')),
                ('menos50k', _('Menos de $50,000')),
                ('50k-100k', _('$50,000 - $100,000')),
                ('100k-250k', _('$100,000 - $250,000')),
                ('250k-500k', _('$250,000 - $500,000')),
                ('500k-1m', _('$500,000 - $1,000,000')),
                ('mas1m', _('Más de $1,000,000')),
            ]),
        }