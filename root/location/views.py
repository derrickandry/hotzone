from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import locationSearchForm, searchResultsForm
from urllib.parse import quote
import requests
# Create your views here.

def location_view(request, *args, **kwargs):

	if request.method == 'POST':
		searchResults = searchResultsForm(request.POST)
		if searchResults.is_valid():
			searchResults.save()
			return HttpResponse("<script> alert('Location Saved!'); window.location.href = '/location'</script>")
		else:
			return HttpResponse("<script> alert('Error! Choose another locatio!n'); window.location.href = '/location'</script>")
	else:
		if request.GET:
			locationQuery = request.GET['locationQuery']
			searchForm = locationSearchForm(request.GET)
			api_address = "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + quote(locationQuery)
			result = requests.get(api_address)
			if (result.status_code) == 400:
				return HttpResponse("<script> alert('Invalid query! Use different keywords!'); window.location.href = '/location'</script>")
			elif (result.status_code) == 500:
				return HttpResponse("<script> alert('GeoData is down! Try again later'); window.location.href = '/location'</script>") 
			data_json = (result).json()[0]
			searchResults = searchResultsForm(initial=
												{
													'location': data_json['nameEN'], 
													'address': data_json['addressEN'],
													'x_coor': data_json['x'],
													'y_coor': data_json['y']
												}
											 )


		else:

			searchForm = locationSearchForm()
			searchResults = None

	return render(request, 'location.html', {'locationSearchForm': searchForm, 'searchResults':searchResults})


	