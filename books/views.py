from django.shortcuts import render_to_response,render

# Create your views here.

from django.db.models import Q
from books.models import Book,Author,Publisher
from books.forms import ContactForm,PublisherForm
from django.http import HttpResponseRedirect,HttpResponse

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
            )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html", {
        "results": results,
        "query": query
        })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            con=form.save()
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request,'contact.html', {'form': form})

def thanks(request):
    html='<html>Thanks</html>'
    return HttpResponse(html)

def pub_new(request):
    if request.method=='POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            pub=form.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = PublisherForm()
    return render(request,'pub_edit.html', {'form': form})

def currentbook(request):
    query=request.GET.get('q','')
    book=Book.objects.get(title__exact=query)
    publisher=Publisher.objects.get(book__title__exact=query)
    author=Author.objects.get(book__title__exact=query)
    return render(request,'currentbook.html',{'book':book,'publisher':publisher,'author':author})
        
