from django import forms

class toDoForm(forms.Form):
    text = forms.CharField(max_length=150,widget=forms.TextInput( attrs={'class':'form-control','placeholder':'Enter todo e.g. Delete junk files', 'aria-label':'Todo','aria-describedby':'add-btn'} ))
