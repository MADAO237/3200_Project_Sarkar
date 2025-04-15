import requests

BASE = "http://localhost:4000/orders"

def print_result(name, res):
    try:
        body = res.json()
    except:
        body = res.text
    print(f"[{res.status_code}] {name}: {body}")

# 1. Pickup Time
res = requests.post(f"{BASE}/pickup_time", json={
    "pickup_time": "2025-04-15 12:00:00"
})
print_result("Pickup Time", res)

# 2. Delivery Time
res = requests.post(f"{BASE}/delivery_time", json={
    "order_id": 1,
    "delivery_time": "2025-04-15 15:00:00"
})
print_result("Delivery Time", res)

# 3. Delivery Location
res = requests.post(f"{BASE}/delivery_location", json={
    "order_id": 1,
    "delivery_location": "Damian's Ski House"
})
print_result("Delivery Location", res)

# 4. Order Details
res = requests.get(f"{BASE}/orderdetails/1")
print_result("Order Details", res)

# 5. Update Cost
res = requests.put(f"{BASE}/1/update_cost", json={
    "total_cost": 29.99
})
print_result("Update Cost", res)

# 6. Order Status
res = requests.get(f"{BASE}/1/status")
print_result("Order Status", res)
