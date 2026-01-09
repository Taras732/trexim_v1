from django.shortcuts import render
from django.http import HttpResponse
from . import calculators

def home(request):
    return render(request, 'home.html')

def smart_tools_distance(request):
    if request.method == "POST":
        city_a = request.POST.get('city_a')
        city_b = request.POST.get('city_b')
        cargo_type = request.POST.get('cargo_type')
        
        result = calculators.calculate_distance(city_a, city_b, cargo_type)
        
        return render(request, 'partials/tool_result_distance.html', {'result': result})
    return HttpResponse("")

def smart_tools_cost(request):
    if request.method == "POST":
        weight = request.POST.get('weight', 0)
        volume = request.POST.get('volume', 0)
        fuel = request.POST.get('fuel', 'diesel')
        distance = request.POST.get('distance', 100)
        
        result = calculators.calculate_cost(weight, volume, fuel, distance)
        
        return render(request, 'partials/tool_result_cost.html', {'result': result})
    return HttpResponse("")

def smart_tools_currency(request):
    if request.method == "POST":
        amount = request.POST.get('amount', 0)
        currency = request.POST.get('currency', 'USD')
        
        result = calculators.calculate_currency(amount, currency)
        
        return render(request, 'partials/tool_result_currency.html', {'result': result})
    return HttpResponse("")
