import json, time, random, os
from datetime import datetime

os.makedirs("data/raw/clickstream", exist_ok=True)

while True:
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "user_id": random.randint(1, 100),
        "event_type": random.choice(["view_product", "add_to_cart", "purchase"]),
        "product_id": random.randint(1, 30)
    }
    with open(f"data/raw/clickstream/event_{int(time.time()*1000)}.json", "w") as f:
        json.dump(event, f)
    time.sleep(2)