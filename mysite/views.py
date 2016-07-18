from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
#def current_datetime(request):
    #now = datetime.datetime.now()
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)

#def hours_ahead(request,offset):
    #offset=int(offset)
    #dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    #html="<html><body>In %s hour(s),It will be %s.</body></html>" %(offset, dt)
    #return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def hours_ahead(request,offset):
    offset=int(offset)
    dt=datetime.datetime.now()+datetime.timedelta(hours=offset)
    t=get_template('hours_ahead.html')
    html=t.render(Context({'hour_offset':offset,'next_time':dt}))
    return HttpResponse(html)

###################GENERATING PDF's#######################
from reportlab.pdfgen import canvas

def pdf_view(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment;filename="helloworld.pdf"'
    p=canvas.Canvas(response)
    p.drawString(100, 100, "Hello Shubhanker.")
    p.showPage()
    p.save()
    return response


