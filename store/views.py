from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import MobileForm
from .models import Mobile


def add_mobile(request):
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_mobiles")
    else:
        form = MobileForm()
    return render(request, "add_mobile.html", {"form": form})


def list_mobiles(request):
    mobiles = Mobile.objects.all()
    return render(request, "list_mobiles.html", {"mobiles": mobiles})


def report_korea_nationality(request):
    korean_mobiles = Mobile.objects.filter(nationality="korea")
    print
    data = [
        {"model": mobile.model, "brand_name": mobile.brand_name, "country_producer": mobile.country_producer}
        for mobile in korean_mobiles
    ]
    return JsonResponse(data, safe=False)


def report_brand_mobiles(request):
    if request.method == "GET":
        brand_name = request.GET.get("brand_name")
        brand_mobiles = Mobile.objects.filter(brand_name=brand_name)
        data = [
            {"model": mobile.model, "brand_name": mobile.brand_name, "country_producer": mobile.country_producer}
            for mobile in brand_mobiles
        ]
        return JsonResponse(data, safe=False)


def report_same_country_nationality(request):
    mobiles = Mobile.objects.filter(
        country_producer=F("nationality")  # اینجا کشور سازنده و ملیت برابر هم باشند
    ).values()
    return JsonResponse(list(mobiles), safe=False)
