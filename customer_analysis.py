# customer_analysis.py
# Analyse de comportement client - Projet Data Analyst
# Auteur : StanyNilaina


# === 1. IMPORTATION DES LIBRAIRIES ===
import pandas as pd
import matplotlib.pyplot as plt

# === 2. CHARGEMENT DES DONNÉES ===
df = pd.read_csv("data/purchase_behavior.csv", parse_dates=['purchase_date'])

# === 3. FEATURE ENGINEERING ===
df['purchase_day'] = df['purchase_date'].dt.day_name()
df['avg_basket'] = df['total_amount'] / df['quantity']
df['date_only'] = df['purchase_date'].dt.date

# === 4. ANALYSE 1 : Ventes par jour de la semaine ===
sales_by_day = df.groupby('purchase_day')['total_amount'].sum().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
])
plt.figure(figsize=(10, 6))
sales_by_day.plot(kind='bar', color='skyblue')
plt.title("Total des ventes par jour")
plt.xlabel("Jour")
plt.ylabel("Ventes (€)")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("figures/ventes_jour.png")
plt.show()

# === 5. ANALYSE 2 : Histogramme des paniers ===
plt.figure(figsize=(10, 6))
df['avg_basket'].hist(bins=30, color='coral', edgecolor='black')
plt.title("Distribution des paniers moyens")
plt.xlabel("Panier moyen (€)")
plt.ylabel("Nb clients")
plt.grid(axis='x')
plt.tight_layout()
plt.savefig("figures/paniers_moyens.png")
plt.show()

# === 6. ANALYSE 3 : Top produits par revenus ===
top_products = df.groupby('product_category')['total_amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar', color='mediumseagreen')
plt.title("Top catégories Produits")
plt.xlabel("Chiffre d'affaires (€)")
#plt.gca().invert_yaxis()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("figures/top_produits_category.png")
plt.show()

# === 7. ANALYSE 4 : Meilleurs clients ===
top_clients = df.groupby('customer_id')['total_amount'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_clients.plot(kind='bar', color='gold')
plt.title("Top 10 Clients")
plt.xlabel("ID Client")
plt.ylabel("Total dépensé (€)")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("figures/top_clients.png")
plt.show()

# === 8. ANALYSE 5 : Ventes dans le temps ===
sales_over_time = df.groupby('date_only')['total_amount'].sum()
plt.figure(figsize=(14, 6))
sales_over_time.plot(color='dodgerblue')
plt.title("Ventes quotidiennes")
plt.xlabel("Date")
plt.ylabel("CA (€)")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/ventes_temps.png")
plt.show()
