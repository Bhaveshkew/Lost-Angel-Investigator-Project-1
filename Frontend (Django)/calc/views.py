
from django.http import HttpResponse
from django.shortcuts import render , redirect
from LostAngelFinder.settings import MEDIA_ROOT
from calc.forms import PersonForm
from calc.machinelearning import pipeline_model
from django.conf import settings
from calc.models import Person, RegisteredChild,User
import cv2
import os

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['fname']
        email = request.POST['email']
        npass = request.POST['npass']
        cpass = request.POST['cpass']
        # age = request.GET['age']
        mobile = request.POST['mobile']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        aadhar = request.POST['aadhar']
        if npass == cpass:
            ins = User.objects.create(unique_id = aadhar , name = name ,password = npass, email = email , country = country , state = state , city = city , mobile = mobile)
            return redirect(printt)
        else:
            print("ERROR")
    return render(request, 'register.html')

def printt(request):
    form = PersonForm()
    if request.method == "POST":
        form = PersonForm(request.POST or None ,request.FILES or None)
        if form.is_valid():
            save = form.save(commit=True)
            pk = save.pk
            image_obj = Person.objects.get(pk = pk)
            fileroot = str(image_obj.image)
            filepath = os.path.join(settings.MEDIA_ROOT , fileroot)
            print(filepath)
            img , cnt ,score= pipeline_model(filepath)
            
            if score*100<30:
                return render(request, 'notfound.html')
            detected_person = RegisteredChild.objects.get(pk = cnt)
            path_to_send= ".." + detected_person.image.url
            return render(request , 'home.html' , {'detected_person' : detected_person , 'path': path_to_send,"path1":filepath})
            
    return render(request , 'upload.html' , {'form':form})