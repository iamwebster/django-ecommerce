from django import forms 


class CreateOrderForm(forms.Form):
    '''The form for creation a new user'''
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    need_delivery = forms.ChoiceField(choices=(
        ('0', False),
        ('1', True),
    ))
    delivery_address = forms.CharField(required=False)
    payment_on_delivery = forms.ChoiceField(choices=(
        ('0', False),
        ('1', True),
    ))


    def clean_phone_number(self):
        '''The method for validate phone number field'''
        data = self.cleaned_data['phone_number']

        if not data.isdigit():
            raise forms.ValidationError('Phone number must contain only digits!')
        
        return data