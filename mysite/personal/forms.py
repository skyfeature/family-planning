from django import forms
from django.utils.safestring import mark_safe

class YearForm(forms.Form):
	y2011 = forms.BooleanField(required=False, label="2011")
	y2012 = forms.BooleanField(required=False, label="2012")
	y2013 = forms.BooleanField(required=False, label="2013")

class ContraceptiveMethod(forms.Form):
	femaleSterilisation = forms.BooleanField(required=False, label="Female Sterilisation")
	condomUse = forms.BooleanField(required=False, label="Condom Use")

class Y_variable(forms.Form):
	yCHOICES = (('1', 'Condom',), ('2', 'Insurance',), ('3', 'TFR',), ('4', 'Birth Control Pills',), ('5', 'Tubectomy',), ('6', 'CopperT',), ('7', 'HAF during Diarrhoea',), ('8', 'Aware about ORT and ORS',), ('9', 'Aware about ORT, ORS and Zinc',))
	y_axis = forms.ChoiceField(widget=forms.RadioSelect, choices=yCHOICES, label=mark_safe("<strong>Choose Y variable</strong>"))
	xCHOICES = (('1', 'Education',), ('2', 'Religion',), ('3', 'District',))
	x_axis = forms.ChoiceField(widget=forms.RadioSelect, choices=xCHOICES, label=mark_safe("<strong>Choose X variable</strong>"))

# class DemoVariable(forms.Form):
# 	CHOICES = (('1', 'Education',), ('2', 'Religion',), ('2', 'District',))
# 	x_axis = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, label="Choose X axis")