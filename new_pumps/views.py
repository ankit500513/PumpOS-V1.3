from django.shortcuts import render

# Create your views here.
from django.db.models import Sum
from datetime import date
from .models import Pump
from .models import Nozzle
from .models import DailySale
from django.contrib.auth.decorators import login_required

def pump_list(request):
    pumps = Pump.objects.all()
    return render(request, 'new_pumps/pump_list.html', {'pumps': pumps})


def nozzle_list(request):
    nozzles = Nozzle.objects.all()
    return render(request, 'new_pumps/nozzle_list.html', {'nozzles': nozzles})

@login_required
def sale_list(request):
    sales = DailySale.objects.all().order_by('-sale_date')
    return render(request, 'new_pumps/sale_list.html', {'sales': sales})

@login_required
def dashboard(request):
    today = date.today()
    today_sales = DailySale.objects.filter(sale_date=today).aggregate(total=Sum('total_amount'))['total'] or 0
    pumps = Pump.objects.count()
    nozzles = Nozzle.objects.count()
    recent_sales = DailySale.objects.order_by('-sale_date')[:5]
    
    return render(request, 'new_pumps/dashboard.html', {
        'today_sales': today_sales,
        'pumps': pumps,
        'nozzles': nozzles,
        'recent_sales': recent_sales
    })