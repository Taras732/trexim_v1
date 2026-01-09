import random
from decimal import Decimal

def calculate_distance(city_a, city_b, cargo_type):
    """
    Mock calculation for distance and time.
    In a real app, this would use Google Maps API or similar.
    """
    # Deterministic "random" based on city names hash to keep it consistent-ish
    seed = hash(f"{city_a}{city_b}")
    random.seed(seed)
    
    distance = random.randint(300, 1200) # km
    avg_speed = 70 # km/h
    duration_hours = distance / avg_speed
    
    # "AI Forecast" logic
    traffic_factor = random.choice([0.9, 1.0, 1.1, 1.2]) # 0.9 = fast, 1.2 = traffic
    adjusted_duration = duration_hours * traffic_factor
    
    hours = int(adjusted_duration)
    minutes = int((adjusted_duration - hours) * 60)
    
    return {
        "distance_km": distance,
        "duration": f"{hours}h {minutes}m",
        "traffic_status": "Heavy Traffic" if traffic_factor > 1.1 else "Normal Flow" if traffic_factor > 0.95 else "Clear Route",
        "ai_note": "Route optimized by Trexim AI based on current road conditions."
    }

def calculate_cost(weight, volume, fuel_type, distance):
    """
    Calculate delivery cost and potential savings.
    """
    base_rate_per_km = 1.5 # USD per km
    weight_factor = float(weight) * 0.05
    volume_factor = float(volume) * 0.02
    
    fuel_multiplier = 1.0
    if fuel_type == 'diesel':
        fuel_multiplier = 1.1
    elif fuel_type == 'electric':
        fuel_multiplier = 0.8
        
    estimated_cost = (base_rate_per_km * float(distance)) + weight_factor + volume_factor
    estimated_cost *= fuel_multiplier
    
    # Trexim usually saves ~15% via optimization
    trexim_saving = estimated_cost * 0.15
    trexim_final = estimated_cost - trexim_saving
    
    return {
        "market_price": round(estimated_cost, 2),
        "trexim_price": round(trexim_final, 2),
        "savings": round(trexim_saving, 2),
        "percent_saved": "15%"
    }

def calculate_currency(amount, currency_type):
    """
    Mock currency conversion.
    """
    amount = float(amount)
    rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'UAH': 41.5,
        'GBP': 0.78
    }
    
    target_currency = 'USD' # converting to USD base for internal view
    if currency_type in rates:
        rate = rates[currency_type]
        converted = amount / rate if currency_type != 'USD' else amount
    else:
        converted = amount
        
    # Cashless speed logic
    transfer_speed = "Instant" if amount < 10000 else "15-30 mins"
    
    return {
        "original_amount": amount,
        "currency": currency_type,
        "converted_usd": round(converted, 2),
        "rate_used": rates.get(currency_type, 1.0),
        "transfer_speed": transfer_speed
    }
