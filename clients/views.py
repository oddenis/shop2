from django.shortcuts import render
from .models import Client
from .forms import ClientForm
# Create your views here.



def clients(request):

    clients = Client.objects.all()
    form = ClientForm
    context = {
        'client':clients,
        'form':form
               }

    if request.method == 'POST':
        dataform = ClientForm(request.POST)
        if dataform.is_valid():
            # f_f_name=dataform.cleaned_data['first_name']
            # f_l_name=dataform.cleaned_data['last_name']
            # f_phone=dataform.cleaned_data['phone']
            # f_mail=dataform.cleaned_data['email']
            # data = Client(first_name=f_f_name, last_name=f_l_name, phone=f_phone, email=f_mail)
            # data.save()
            dataform.save()
    return render(request, 'clients/clients.html', context)