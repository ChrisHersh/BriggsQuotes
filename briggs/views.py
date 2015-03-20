from django.shortcuts import render, redirect
from django.http import HttpResponse
from briggs.models import BriggsQuote
import re

# Create your views here.

def index(request):
	if request.method == 'POST':
		return submit(request)
	else:
		return render(request, 'briggs/index.html', {'quotes': getQuotesText() }) 

def submit(request):
	quote = ""
	prevPage = ""
	try:
		quote=request.POST['new_quote']
		addQuote(quote)
	except:
		pass

	try:
		return redirect(request.POST['referer'])
	except:
		return teapot()

def addQuote(quote):
	quote = re.sub(r"[<>\\/~]", " ", quote)
	qu = BriggsQuote(quote_text=quote)
	qu.save()

def getQuotesText():
	allQuotes = BriggsQuote.objects.filter(visible=True)

	listOfQuotes = []
	for x in allQuotes:
		listOfQuotes.append(str(x.quote_text))

	return listOfQuotes

def view(request):
	quotes = ""
	for x in getQuotesText():
		quotes += x + "<br>"

	return HttpResponse(quotes)

def teapot():
	return HttpResponse("Error 418 - I'm a Teapot", status=418)
