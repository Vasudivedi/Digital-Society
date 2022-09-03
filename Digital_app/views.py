from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
default_data = {}

def register_page(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def home_page(request):
    return render(request,'home_page.html')



#Register Functionality
def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        data = Registered_user.objects.create(email=email, password = password)
        User_data.objects.create(Registered_user=data)
    return render(request,'register.html', default_data)


def profile_page(request):
    profile_data_load(request)
    return render(request,'profile_page.html', default_data)  
    
 #Load profile data
def profile_data_load(request):
    r_user = Registered_user.objects.get(email = request.session['email'])
    profile_data = User_data.objects.get(Registered_user = r_user)
    default_data['profile_data'] = profile_data


#Login functionality

def handle_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = Registered_user.objects.get(email = email)
            if user.password == password:
                request.session['email'] = email        #session creation
                return redirect(profile_page)
            else:
                print('incorrect password')

        except Registered_user.DoesNotExist as err:
            print('record not found!', err)
    
    return redirect(login)

def profile_update(request): 
    if request.method == "POST":
        r_user = Registered_user.objects.get(email = request.session['email'])
        profile_data = User_data.objects.get(Registered_user = r_user)

        profile_data.name = request.POST['name']
        profile_data.address = request.POST['address']
        profile_data.country = request.POST['country']
        profile_data.dob = request.POST['dob']
        profile_data.phone = request.POST['phone']
        profile_data.gender = request.POST['gender']
        profile_data.member = request.POST['member']
        profile_data.alternate_contact_no = request.POST['alternate_contact_no']
        profile_data.vehicle_no = request.POST['vehicle_no']
        profile_data.total_vehicle = request.POST['total_vehicle']
        profile_data.profile_image = request.FILES['profile_image']
        

        profile_data.save()
     
        return redirect(profile_page)


#Logout Functionality
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(login)        

def contact_page(request):
    return render(request,'contact.html',default_data)


#Send mail functionality

@csrf_exempt
def mail_send(request):
    email_to_list = [request.POST['email'],]

    from_email = settings.EMAIL_HOST_USER

    subject = request.POST['subject']

    message = request.POST['message']

    send_mail(subject, message, from_email, email_to_list)

    return redirect(contact_page)

#upload image
def upload_image(request):
    pass 

def about_us(request):
    return render(request,'about.html',default_data)