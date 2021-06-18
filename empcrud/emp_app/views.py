from django.shortcuts import render,HttpResponseRedirect

from .forms import EmpRegistration

from .models import Emp

# add and show
def add_show(request):
    if request.method == 'POST':
        fm = EmpRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Emp(name=nm,email=em,password=pw)
            reg.save()
            fm = EmpRegistration()
            # fm.save()
    else:
        fm = EmpRegistration()
    empl = Emp.objects.all()
    return render(request, 'emp_app/addandshow.html',{'form':fm,'emp':empl})

# Update
def update_data(request,id):
    if request.method == 'POST':
        pi = Emp.objects.get(pk=id)
        fm = EmpRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Emp.objects.get(pk=id)
        fm = EmpRegistration()
    return render(request,'emp_app/updateemp.html', {'form':fm})

# Delete 
def delete_data(request,id):
    if request.method == 'POST':
        pi = Emp.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')