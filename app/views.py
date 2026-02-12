from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    return render(req,'register.html')

def login(req):
    return render(req,'login.html')

def Register_data(req):
    if req.method=='POST':
        n=req.POST.get('Name')
        e=req.POST.get('Email')
        c=req.POST.get('City')
        a=req.POST.get('Age')
        co=req.POST.get('Contact')
        i=req.FILES.get('Image')
        p=req.POST.get('Password')
        cp=req.POST.get('Cpassword')
        print(n,e,c,a,co,i,p,cp)

        user = Student.objects.filter(Email=e)
        if user.exists():
            msg = "Already exist"
            return render(req, 'register.html', {'msg': msg})   # ✅ FIXED
        else:
            if p == cp:
                Student.objects.create(
                    Name=n, Email=e,City=c,Age=a,Contact=co,Image=i,Password=p, Cpassword=cp,)
                return redirect('login')

            else:
                userdata = {'Name': n, 'Email': e, 'Contact': c}
                msg = "Password and Confirm Password not match"
                return render(req, 'register.html', {'pmsg': msg, 'data': userdata})
    return render(req, 'login.html')

def login_data(req):
    e=req.POST.get('Email')
    p=req.POST.get('Password')
    if e=='admin@gmail.com' and p=='admin':
        a_data={    
                'id':1,
                'name':'admin',
                'email':'admin@gmail.com',
                'Password':'admin'}
        req.session['a_data']=[a_data]
        return redirect('admindash')
    elif req.method=="POST":
        e=req.POST.get('Email')
        p=req.POST.get('Password')
        user=Student.objects.filter(Email=e)
                #  print(user)
        if not user:
            msg="Register First"
            return redirect('register')
        else:
            userdata=Student.objects.get(Email=e)
        if p==userdata.Password:
            req.session['user_id']=userdata.id
            return redirect('userdash')
        else:
            msg='Email & password not match'
            return render(req,'login.html',{'pmsg':msg})
    return render(req,'login.html')

def userdash(req):
    return render(req,'userdash.html')

def admindash(req):
    return render(req,'admindash.html')

def userdash(req):
   if 'user_id' in req.session:
     id=req.session.get('user_id')
     userdata=Student.objects.get(id=id)
     return render(req,'userdash.html',{'data':'userdata'})

def logout(req):
    if 'user_id' in req.session:
        req.session.flush()
    return redirect('login')
    