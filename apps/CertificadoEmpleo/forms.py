from django import forms


class DatosForm(forms.Form):
    cedula = forms.CharField(max_length=15)


    def clean(self):
        clean_data=super(DatosForm,self).clean()

