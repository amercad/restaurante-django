from django import forms

class FormularioPlatos(forms.Form):

    PLATOS = (
        (1, 'Entradas'),
        (2, 'Platos fuerte'),
        (3, 'Postres')
    )

    nombre = forms.CharField(
        required=True,
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    descripcion = forms.CharField(
        required=False,
        max_length=250,
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'})
    )
    fotografia = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    precio = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'})
    )
    tipo = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': 'form-control mb-3'}),
        choices=PLATOS
    )