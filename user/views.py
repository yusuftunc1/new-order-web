from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #kullanıcı adı ve şifresi eşleşen bir kullanıcı varsa obje olarak döndürme
        user = auth.authenticate(username= username, password= password)
        #döndürülen objeyi kontrol etme
        if user is not None:
            #session oluşturma
            auth.login(request, user)
            #mesaj ekleme
            messages.add_message(request, messages.SUCCESS, "Giriş başarılı")
            ### yetki kontrolu eklenecek
            return redirect('teslim', user.id)
        else:

            messages.add_message(request, messages.ERROR, 'kullanıcı adı ve ya paralo yanlış')
            return redirect('login')

    else:
        #eğer sayfa ilk kez açılıyorsa ve bir post değeri gönderilmediyse sayfa açılmalı
        return render(request, 'user/login.html')



def register(request):

    if (request.method == 'POST'):
        
        #form değerlerini alma
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST["repassword"]

        #şifre kontol
        if password == repassword:
            #username kontrol
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, "bu kullanıcı adı daha önce alınmış" )

                return redirect('register')
            else:
                #mail kontrol
                if User.objects.filter(email = email).exists():
                    
                    messages.add_message(request, messages.WARNING, "bu mail daha önce alınmış")
                    return redirect('register')
                else:
                    #okey create user
                    user = User.objects.create_user(username= username, password= password, email= email)
                    user.save()
                    
                    messages.add_message(request, messages.SUCCESS, 'kullanıcı oluşturuldu')
                    return redirect('login')
        else:
            messages.add_message(request, messages.WARNING, "paralolar eşleşmiyor")

            return redirect('register')

    else:
        return render(request, 'user/register.html')




def logout(request):

    if request.method == 'POST':
        #session id silme
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, "Oturumunuz kapatıldı")
        return redirect('logout')

    return render(request, 'user/logout.html')


