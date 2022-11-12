from django import forms

class FormularioEmpleados(forms.Form):

    CARGO = (
        (1, 'Adminidtrador'),
        (2, 'Ayudante'),
        (3, 'Cheff'),
        (4, 'Mesero')
    )

    nombre = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    apellidos = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    fotografia = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    cargo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        choices=CARGO
    )
    salario = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'})
    )
    contacto = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'}),
    )