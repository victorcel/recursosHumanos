from django import forms


class DatosForm(forms.Form):
    cedula = forms.IntegerField()

    def clean(self):
        clean_data=super(DatosForm,self).clean()

