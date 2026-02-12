from django.shortcuts import render
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
    Student.objects.create(Name=n,Email=e,City=c,Age=a,Contact=co,Image=i,Password=p,Cpassword=cp,)
    

    return render(req,'login.html')




# def all(req):
#     data=Employe.objects.all()
#     print(data)
#     return render(req,'landing.html',{"data": all})
    