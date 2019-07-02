from django import forms


class PurchasePointsForm(forms.Form):
		Enter_Points_to_be_purchase  = forms.IntegerField(min_value=1, widget=forms.NumberInput(
                attrs={'size':'10'}),initial=500)
		
