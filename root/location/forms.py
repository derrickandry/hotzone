from django import forms
from .models import Location

class locationSearchForm(forms.Form):
	locationQuery = forms.CharField(label="Search a location", max_length=100)

class searchResultsForm(forms.ModelForm):

	def __init__(self, *args, **kwargs): 
	    super(searchResultsForm, self).__init__(*args, **kwargs)                       
	    # self.fields['location'].disabled = True
	    # self.fields['address'].disabled = True
	    # self.fields['x_coor'].disabled = True
	    # self.fields['y_coor'].disabled = True

	    self.fields['location'].widget.attrs.update(size=100, readonly=True)
	    self.fields['address'].widget.attrs.update(size=100, readonly=True)
	    self.fields['x_coor'].widget.attrs.update(readonly=True)
	    self.fields['y_coor'].widget.attrs.update(readonly=True)
	class Meta:
		model = Location
		fields = [
				'location',
				'address',
				'x_coor',
				'y_coor'
		] 
	
	# name = forms.CharField(label="Name", max_length=100)
	# address = forms.CharField(label="Address", max_length=200)
	# x_coor = forms.DecimalField(label = "X-Coordinates", max_digits = 7, decimal_places = 0)
	# y_coor = forms.DecimalField(label = "Y-Coordinates", max_digits = 7, decimal_places = 0)
