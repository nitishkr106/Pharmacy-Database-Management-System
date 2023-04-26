from django import forms
from .fields import ListTextWidget
from .models import Company, Product, Sales, Supplier,Contact, Patient, Employee, SupplierInvoice
from django.forms import ModelForm, DateInput


class FormsetForm(forms.Form):
    delete = forms.BooleanField(required=False, initial=False)
    # some other fields with data

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name',)

class QtyForm(forms.Form):
    value = forms.IntegerField()

class BillForm(ModelForm):
    name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}))
    class Meta:
        model = Product
        fields=('name',)

    def __init__(self, *args, **kwargs):
      _company_list = kwargs.pop('data_list', None)
      super(BillForm, self).__init__(*args, **kwargs)
      self.fields['name'].widget = ListTextWidget(
          data_list=_company_list, name='name-list')

class FormForm(ModelForm):
    company = forms.CharField(required=True)
    mfg = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    exp = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    class Meta:
        model = Product
        fields= '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}),
            'batch_no': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter Numbers Only'}),
        }
          
    def __init__(self, *args, **kwargs):
      _company_list = kwargs.pop('data_list', None)
      super(FormForm, self).__init__(*args, **kwargs)
      self.fields['company'].widget = ListTextWidget(data_list=_company_list, name='company-list')

class ProductForm(ModelForm):
    mfg = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    exp = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    class Meta:
        model = Product
        fields= ('mfg','exp','cost','selling_price','qty','supplier')


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields= '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter Numbers Only'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields= '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields= '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter Numbers Only'})
        }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields= '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter Numbers Only'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern':'[A-Za-z ]+', 'title':'Enter Characters Only'})
        }

class SupplierInvoiceForm(ModelForm):
    order_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    delivery_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', }))
    class Meta:
        model = SupplierInvoice
        fields = '__all__'

        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter Numbers Only'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off','pattern':'[0-9]+', 'title':'Enter Numbers Only'}),
        }