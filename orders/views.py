from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from matplotlib.style import context
from .models import orders
from datetime import date, datetime
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request, "orders/homepage.html")


def authorizedUser(request, id):
    
    users = User.objects.filter(id = id)
    for user in users:
        if(user.is_superuser):
            order = orders.objects.all()

            context= {
                'orders' : order
            }
            return render(request, "orders/authorizedUser.html", context)
        else:
            return render(request, "orders/homepage.html")


def searchdate(request):
    
    if(request.method == 'POST'):
        appointmentdate = request.POST['appointmentdate']
        order = orders.objects.filter(appointmentdate = appointmentdate)
        
        context = {
            'orders' : order
        }
        return render(request, "orders/authorizedUser.html", context)
    else:
        return redirect('home')



def search(request):
    
    if(request.method == 'POST'):
        username = request.POST['username']
        order = orders.objects.filter(name = username)
        
        context = {
            'orders' : order
        }
        return render(request, "orders/authorizedUser.html", context)
    else:
        return redirect('home')




def teslim(request , id):
    #bugünün tarihini alma
    todayy = datetime.today()
    bugun = date( todayy.year, todayy.month, todayy.day)

    #kullanıcıya ait order var mı?
    if orders.objects.filter(userid = id).exists():
        try:
            order = orders.objects.filter(userid= id)  
        except orders.DoesNotExist:
            raise Http404("aradığınız kayıt yok")

        context = {
            'orders' : order
        }
        #geçen günü hesaplama
        for i in order:
            if i.startingdate == None:
                pass
            else:
                daycount = (bugun - i.startingdate ).days
                orders.objects.filter(id = i.id).update(daycount = daycount)
            
            if i.appointmentdate == None:
                pass
            else:
                remainingday = (i.appointmentdate - bugun).days
                orders.objects.filter(id = i.id).update(remainingday = remainingday)       
        return render(request, "orders/mainpage.html", context)
    else:
        return render(request, "orders/mainpage.html")

    
  
def addAppointment(request, id):
    
    if(request.method == 'POST'):
        #order.id ve seçilen tarih değerini alma
        id = request.POST['id']
        appointmentdate = request.POST['appointmentdate']
        appdate = []
        appdate = appointmentdate.split('-')
        appdates = date(int(appdate[0]),int(appdate[1]),int(appdate[2]))

        order = orders. objects.filter(id = id)
        for i in order:
            userid = i.userid
            numofproduct = i.numofproduct
            day = (appdates - i.startingdate).days

        dates = orders.objects.filter(appointmentdate = appdates)
        koli = 0
        for a in dates:
            koli = koli + a.numofproduct
        koli = koli + numofproduct

        if(koli > 101):
            messages.add_message(request, messages.ERROR, f'{appdate[2]}-{appdate[1]}-{appdate[0]} dolu. Toplam : {koli} koli. 5000 den fazla olamaz. Lütfen farklı bir gün seçiniz')
            return redirect('teslim', userid )
        else:
            if (day > 96):
                #database de randevu tarihini güncelleme
                orders.objects.filter(id = id).update(appointmentdate = appointmentdate)
                messages.add_message(request, messages.SUCCESS, 'randevu oluşturuldu')
                return redirect('teslim', userid )
            else:
                messages.add_message(request, messages.ERROR, 'kurumada geçen gün en az 97 gün olmalıdır')
                return redirect('teslim', userid )   
    else:
        messages.add_message(request, messages.ERROR, 'Something went wrong')
        return redirect('teslim', userid )



def deleteAppointment(request, id):
    #user id alma
    order = orders. objects.filter(id = id)
    for i in order:
        userid = i.userid

    #randevu tarihinin ve kalan günün boş bir değere update etme
    orders.objects.filter(id = id).update(appointmentdate = None)
    orders.objects.filter(id = id).update(remainingday = None)
    messages.add_message(request, messages.SUCCESS, 'randevu silindi')

    return redirect('teslim', userid )


