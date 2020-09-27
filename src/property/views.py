from django.shortcuts import render

# Create your views here.
from .models import Property , Category
from .forms import ReserveForm
from django.db.models import Q
def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'


    adress_query = request.GET.get('q')
    property_type = request.GET.getlist('property_type' , None)
    if adress_query and property_type :
        property_list = property_list.filter(
            Q(adress__icontains = adress_query) &
            Q(type__icontains = property_type[0])
        ).distinct()


    context = {
        'property_list' : property_list
    }

    return render(request, template , context)




def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'


    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()


    else:
        reserve_form = ReserveForm()


    context = {
        'property_detail' : property_detail ,
        'reserve_form' : reserve_form
    }

    return render(request, template, context)
