# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 13:06:33 2025

@author: Stany
"""
import pandas as pd
import numpy as np

df = pd.read_csv('./ecommerce_dataset.csv')
print(df.columns)
df['signup_date'] = pd.to_datetime(df['signup_date'])
df['purchase_date'] = pd.to_datetime(df['purchase_date'])
#extraire les jours et heures des achats
df['purchase_day'] = df['purchase_date'].dt.day_name()
#calcul du panier par client
avg_panier = df.groupby('customer_id')['total_amount'].mean().reset_index()
avg_panier.rename(columns={'total_amount': 'avg_panier'}, inplace=True)
# 4. On fusionne avec le dataset d'origine
df = df.merge(avg_panier, on='customer_id', how='left')
# 5. Vérification
print(df[['customer_id', 'total_amount', 'avg_panier']].head())
print(df[['purchase_day']].sample(5))
