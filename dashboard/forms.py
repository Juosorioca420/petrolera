from django import forms
from .models import Campo, Carrotanque, Territorio, Operador

class IndicadorForm( forms.Form ):
    brent = forms.FloatField()
    TRM = forms.FloatField()

class FacturaForm( forms.ModelForm, forms.Form ):
    class Meta:
        model = Campo
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(FacturaForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ModelChoiceField( queryset = Campo.objects.all().order_by('name') )

    cantidad = forms.FloatField()

class PromedioForm( forms.ModelForm ):
    class Meta:
        model = Campo
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(PromedioForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ModelChoiceField( queryset = Campo.objects.all().order_by('name') )

class CapacidadForm( forms.ModelForm ):
    class Meta:
        model = Territorio
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(CapacidadForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ModelChoiceField( queryset = Territorio.objects.all().order_by('name') )

class OperadorForm( forms.ModelForm ):
    class Meta:
        model = Operador
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super(OperadorForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.ModelChoiceField( queryset = Operador.objects.all().order_by('name') )

class CrudoForm( forms.ModelForm, forms.Form ):
    class Meta:
        model = Campo
        fields = ['crudo_name']

    equiv = forms.FloatField()

class CarroForm( forms.Form ):
    matricula = forms.ModelChoiceField( queryset = Carrotanque.objects.all(), to_field_name="id" )
    name = forms.ModelChoiceField( queryset = Territorio.objects.all().order_by('name'), to_field_name="name" )
