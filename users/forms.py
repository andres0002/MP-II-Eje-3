from django import forms
from users.models import DatosUsuario

class UserForm(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = (
            "cedula",
            "nombre",
            "apellido"
        )
        labels = {
            'cedula': 'cedula usuario',
            'nombre': 'nombre usuario',
            'apellido': 'apellido usuario'
        }

    def __init__(self, *args, **kwargs):
        '''
                Esta funcion se encarga de darle el diseño al formulario.
                :param args: La cantidad de argumentos que recibe.
                :param kwargs: Se encarga de tomar los parametros de la url.
                '''
        super(UserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})