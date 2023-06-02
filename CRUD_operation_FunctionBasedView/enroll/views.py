from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Student
from .models import User



def add_show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            # fm.save()                                         # By this way also we can save data.... OR
            nm = fm.cleaned_data['name']
            eml = fm.cleaned_data['email']
            psw = fm.cleaned_data['password']
            registation = User(name= nm, email= eml, password= psw)
            registation.save()
                    ## after saving data... show empty form to user for new data insert
            # fm = Student()
            return HttpResponseRedirect('/')
    else:
        fm = Student()
            ## extract all data from the database
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'FORM':fm,'data':stud})





def update_data(request, id):
    if request.method == 'POST':                ## Update button ==> POST request
        pi = User.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:                                       ## Edit button ==> GET request 
        pi = User.objects.get(pk=id)
        fm = Student(instance=pi)
    return render(request, 'enroll/update.html', {'FORM':fm})




def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')