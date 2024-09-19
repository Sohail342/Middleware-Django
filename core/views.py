from django.shortcuts import redirect, render
from .form import RegForm
from .models import RegModel
from django.contrib import messages

def formAPI(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            
            # if email and phone number Already Registered
            if RegModel.objects.filter(email=email).exists(): 
                form.add_error('email', 'This email is already registered.')
            if RegModel.objects.filter(phone=phone).exists():
                form.add_error('phone', 'This Phone number is already registered.')
            else:
                reg = RegModel.objects.create(name=name, email=email, password=password, phone=phone)
                reg.save()
                messages.success(request, 'Created successfully')
                return redirect('formAPI')
                
    else:
        form = RegForm()
    return render(request, 'core/index.html', {'form':form})