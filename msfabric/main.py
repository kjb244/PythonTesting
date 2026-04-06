import re

import pandas as pd
import random
from datetime import datetime, timedelta


def generate_feedback_data(order_ids):
    """
    order_ids: A list of OrderIDs to create feedback for.
    """
    data = []
    comments = [
        "Package arrived in great condition.",
        "Delivery was slightly delayed but the product is excellent.",
        "The carrier was very professional.",
        "Item was exactly as described.",
        "Box was a bit dented, but product was fine.",
        "Fastest shipping I have ever had!",
        "Poor communication from the carrier.",
        "Very happy with this purchase."
    ]

    print(f"Generating feedback for {len(order_ids)} orders...")

    for oid in order_ids:
        # Not every customer leaves a review (simulate 70% response rate)
        if random.random() > 0.3:
            data.append({
                "FeedbackID": f"FB-{random.randint(5000, 9999)}",
                "OrderID": oid,
                "CustomerRating": random.randint(3, 5), # 1-5 star scale
                "VerbatimComment": random.choice(comments),
                "RecommendToFriend": random.choice(["Yes", "No", "Maybe"])
            })

    df = pd.DataFrame(data)
    df.to_csv("customer_feedback_surveys.csv", index=False)

# This simulates data coming from a secondary logistics system
# updated to sync with specific order dates and the Northwind Shippers table
def generate_logistics_data(order_data_list, shipper_names):
    """
    order_data_list: A list of dicts containing {'OrderID': x, 'OrderDate': 'YYYY-MM-DD'}
    shipper_names: A list of names from the Northwind 'Shippers' table (e.g., 'Speedy Express')
    """
    data = []

    print(f"Generating logistics for {len(order_data_list)} specific orders...")

    for order in order_data_list:
        # Convert string date to object
        o_date = datetime.strptime(order['OrderDate'], '%Y-%m-%d')

        # LOGIC: Shipment happens 0 to 2 days AFTER the order
        ship_date = o_date + timedelta(days=random.randint(0, 2))

        # LOGIC: Delivery is estimated 3 to 7 days AFTER the shipment
        est_arrival = ship_date + timedelta(days=random.randint(3, 7))

        # LOGIC: 80% of items are already delivered for the demo
        is_delivered = random.random() > 0.2
        actual_arrival = est_arrival if is_delivered else None
        current_status = "Delivered" if is_delivered else random.choice(['In Transit', 'Delayed', 'Customs Hold'])

        data.append({
            "TrackingID": f"TRK{random.randint(10000, 99999)}",
            "OrderID": order['OrderID'],
            "Carrier": random.choice(shipper_names),  # Now pulling from Shippers table names
            "Status": current_status,
            "ShipDate": ship_date.strftime('%Y-%m-%d'),
            "EstimatedArrival": est_arrival.strftime('%Y-%m-%d'),
            "ActualArrival": actual_arrival.strftime('%Y-%m-%d') if actual_arrival else None,
            "CarbonFootprint_kg": round(random.uniform(1.2, 15.5), 2)
        })

    df = pd.DataFrame(data)
    df.to_csv("product_shipping_logistics.csv", index=False)
    print(f"File 'product_shipping_logistics.csv' generated using carriers: {', '.join(shipper_names)}")


if __name__ == "__main__":
    # Standard Shippers from the Northwind Database
    # In Fabric, you could query these directly: SELECT CompanyName FROM Shippers
    northwind_shippers = [
        'Speedy Express',
        'United Package',
        'Federal Shipping',
        'Global Freight Solutions'  # This is the one we added in the previous SQL step
    ]

    mock_orders = []
    with open('data.txt', 'r') as f:
        for line in f:
            line_data: str = line.split('\t')
            line_date: datetime = datetime.strptime(line_data[1].split(" ")[0], "%m/%d/%y")
            mock_orders.append({'OrderID': int(line_data[0]), 'OrderDate': line_date.strftime("%Y-%m-%d")})

    generate_logistics_data(mock_orders, northwind_shippers)

    order_ids = [order['OrderID'] for order in mock_orders]
    generate_feedback_data(order_ids)
