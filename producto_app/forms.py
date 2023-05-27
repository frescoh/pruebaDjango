from django import forms

from producto_app.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('__all__')
        
    def clean_precio(self):
        """
        Valida el precio que el usuario ingresa en el form

        Raises:
            forms.ValidationError: Genera un error cuando el precio es inferior a 100

        Returns:
            float: Precio que el usuario ingresa en el form
        """
        precio= self.cleaned_data['precio']
        if precio <100:
            raise forms.ValidationError('Ingrese un precio valido')
        return precio