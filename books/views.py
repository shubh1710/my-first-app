from django.shortcuts import render_to_response,render

# Create your views here.

from django.db.models import Q
from books.models import Book,Author,Publisher
from books.forms import ContactForm,PublisherForm,RegistrationForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

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
            #con=form.save()
            topic=form.cleaned_data['topic']
            message=form.cleaned_data['message']
            sender=form.cleaned_data['sender']
            send_mail('Feedback from your site: %s'%topic,message,sender,['shubhankergoyal@gmail.com'],fail_silently=False)
            
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

def currentbook(request,id):
    book=Book.objects.get(pk=id)
    author=Author.objects.filter(book=id)
    return render(request,'currentbook.html',{'book':book,'author':author})


def login_view(request):
    if request.method=='POST':
        username = request.POST['Username']
        password = request.POST['Password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request,'home.html',{'user':username},context_instance=RequestContext(request))
            else:
                html='<html>YOUR  ACCOUNT HAS BEEN DISABLED</html>'
                return HttpResponse(html)
        else:
            html='<html>Either your Username or Password is INCORRECT</html>'
            return HttpResponse(html)

    return render(request,'login.html',context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return render(request,'loggedout.html',context_instance=RequestContext(request))

@csrf_protect
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password2'],
                email=form.cleaned_data['email']
                )
            user_save=form.save()
            return HttpResponseRedirect('/register/success')
            #return render(request,'reg_success.html',context_instance=RequestContext(request))
    else:
        form=RegistrationForm()

    return render(request,'register.html',context_instance=RequestContext(request,{'form':form}))

def reg_success(request):
    return render(request,'reg_success.html',context_instance=RequestContext(request))
    

        


        
    

        
        
        
            
            
            
            
        
