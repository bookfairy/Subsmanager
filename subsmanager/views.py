from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm, LoginForm, CustomForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth, messages
from django.template import RequestContext
from .models import Sub, Custom
from django.db.models import Q
from django.contrib.auth.decorators import login_required


# Create your views here.

def checkuser(getusername):
    try: 
        checkuser = User.objects.get(username=getusername)
        if checkuser is not None:
            return True
    except:
        return False
    
def checkemail(getemail):
    try:
        checkemail = User.objects.get(email=getemail)
        if checkemail is not None:
            return True
    except:
        return False

@login_required(login_url='/login')
def home_view(request):
    ctx = {}
    sum = 0
    if request.user:
        Subscriptions = Custom.objects.filter(user_id=request.user.id)
        ctx['subscriptions'] = Subscriptions
        ctx['user_pk'] = request.user.id
        for sub in Subscriptions:
            sum = sum + sub.price
        ctx['sum'] = sum
        
        return render(request, 'subsmanager/home.html', ctx)
    else:
        pass


def create_view(request):
    ctx = {}
    if request.method =="POST":
        # 이미 해당 user가 동일한 sub에 대해 custom을 등록하려는지 검사.
        custom1 = Custom.objects.filter(user_id=request.user)
        custom = custom1.filter(sub=request.POST.get('sub'))
        if custom:
            return redirect('update', custom.first().pk)
        else:
            custom = Custom()
            custom.sub = Sub.objects.get(pk=request.POST.get('sub'))
            custom.user_id = request.user
            custom.period = request.POST.get('period')
            custom.price = request.POST.get('price')
            custom.last_pay = request.POST.get('last_pay')
            custom.save(force_insert=True)
            
            return redirect('detail', custom.pk)
    else:       
        ctx['form'] = CustomForm
    return render(request, 'subsmanager/create.html', ctx)

def update_view(request,custom_pk):
    if request.method == "POST":
        custom = get_object_or_404(Custom, pk=custom_pk)
        form = CustomForm(request.POST, instance=custom)
        if form.is_valid():
            custom = form.save(commit=False)
            custom.user_id = request.user
            custom.save()
            return redirect('detail', custom.pk)
    else:
        custom = get_object_or_404(Custom, pk=custom_pk)
        form = CustomForm(instance=custom)
        return render(request,'subsmanager/update.html', {'form':form})

    
def detail_view(request, custom_pk):
    ctx = {'sub': get_object_or_404(Custom, pk=custom_pk)}
    return render(request, 'subsmanager/detail.html', ctx)

    
def delete(request, custom_pk):
    Custom.objects.get(id=custom_pk).delete()
    return redirect('home')

def signup(request):
    if request.method == "POST":
        if checkuser(request.POST.get('username')):
            messages.error(request, '이미 존재하는 유저 이름입니다.')
            return render(request, 'subsmanager/adduser.html')
        if checkemail(request.POST.get('email')):
            messages.error(request, '이미 사용 중인 이메일입니다.')
            return render(request, 'subsmanager/adduser.html')
        new_user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    else:
        form = UserForm()
        return render(request, 'subsmanager/adduser.html', {'form': form})
    
    
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'subsmanager/login.html', {'form': form})
    
    
def logout(request):
    auth.logout(request)
    return redirect('login')


