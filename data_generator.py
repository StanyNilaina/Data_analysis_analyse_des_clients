# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:01:38 2025

@author: Stany
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Générateur de dates aléatoires
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

# Paramètres
n_rows = 1000
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Listes fictives
genders = ['Male', 'Female']
categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Beauty']
payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer']
devices = ['Mobile', 'Desktop', 'Tablet']

# Génération des données
data = {
    'customer_id': np.random.randint(1000, 2000, n_rows),
    'gender': np.random.choice(genders, n_rows),
    'age': np.random.randint(18, 70, n_rows),
    'signup_date': [random_date(start_date, end_date) for _ in range(n_rows)],
    'purchase_date': [random_date(start_date, end_date) for _ in range(n_rows)],
    'product_category': np.random.choice(categories, n_rows),
    'product_price': np.round(np.random.uniform(10.0, 500.0, n_rows), 2),
    'quantity': np.random.randint(1, 5, n_rows),
    'payment_method': np.random.choice(payment_methods, n_rows),
    'device_type': np.random.choice(devices, n_rows)
}

df = pd.DataFrame(data)
df['total_amount'] = df['product_price'] * df['quantity']
df.to_csv("ecommerce_dataset.csv", index=False)

print("✅ Données générées :")
print(df.head())
