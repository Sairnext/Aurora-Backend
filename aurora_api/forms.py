from django import forms
from .models import Image

class ModelTrainingForm(forms.Form):
    customer_name = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder': 'Customer Name', 'style': 'max-width: 300px;', 'class':'form-control'}))
    intent = forms.FileField(widget=forms.FileInput(attrs={'placeholder': 'Intents File'}))  
    hidden_size = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder': 'Hidden Size', 'style': 'max-width: 300px;', 'class':'form-control'}))
    epochs = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder': 'No of EPOCHS', 'style': 'max-width: 300px;', 'class':'form-control'}))
    batch_size = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder': 'Batch Size', 'style': 'max-width: 300px;', 'class':'form-control'}))
    learning_rate = forms.CharField(widget=forms.TextInput(attrs={'size':25,'placeholder': 'Learning Rate', 'style': 'max-width: 300px;', 'class':'form-control'}))
    
    
class ImageUploadForm(forms.Form):
    class Meta:
        model  = Image
        fields = ('image')
