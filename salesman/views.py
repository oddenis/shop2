from django.shortcuts import render
from .forms import SalesmanForm
from .models import Salesman, Dolgnost

# Create your views here.
def salesman(request):
    salesmans=Salesman.objects.all()
    saleform = SalesmanForm()
    context={'form':saleform, 'salesmans':salesmans}
    if request.method == 'POST':
        saleform = SalesmanForm(request.POST)
        if saleform.is_valid():
            saleform.save()

    return render(request, 'salesman/salesman.html', context)