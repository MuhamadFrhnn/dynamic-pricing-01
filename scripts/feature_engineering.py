# feature_engineering.py
import pandas as pd
import numpy as np
from scipy import stats
import os


#terbaru
def calculate_dynamic_pricing(df, group_cols):
    # Tetap menggunakan pendekatan aggregasi sederhana seperti aslinya
    grouped = df.groupby(group_cols).agg(
        number_of_orders=('order_id', pd.Series.nunique),
        number_of_sellers=('seller_id', pd.Series.nunique),
        historical_cost=('price', 'median')
    ).dropna().reset_index()

    # Hindari pembagian dengan nol (persis seperti kode asli)
    grouped['number_of_sellers'] = grouped['number_of_sellers'].replace(0, 1)

    # Formula multiplier yang lebih dinamis tetapi tetap sederhana
    # Menggunakan akar kuadrat untuk kurva respons yang lebih halus
    demand_factor = np.sqrt(grouped['number_of_orders'])
    supply_factor = np.sqrt(grouped['number_of_sellers'])
    
    # Multiplier dengan range yang lebih luas
    multiplier = (1 + 0.05 * demand_factor) / (1 + 0.05 * supply_factor)
    # MODIFIKASI: Meningkatkan batas atas klip multiplier.
    # Ini mengatasi masalah di mana harga yang diprediksi akan mencapai batas atas
    # untuk jumlah pesanan yang tinggi, karena model kemungkinan besar
    # mempelajari pembatasan ini dari pembuatan data asli.
    # Dengan memungkinkan rentang yang lebih luas, model berpotensi
    # memprediksi harga yang lebih tinggi untuk permintaan yang lebih tinggi.
    multiplier = np.clip(multiplier, 0.8, 2.0)  # Diubah dari 1.2 menjadi 2.0
    
    # Hitung harga disesuaikan (struktur sama dengan asli)
    grouped['adjusted_price'] = grouped['historical_cost'] * multiplier
    grouped['price_multiplier'] = multiplier  # Tambahkan kolom multiplier untuk analisis
    
    return grouped

# def calculate_dynamic_pricing(df, group_cols):
#     # Tetap menggunakan pendekatan aggregasi sederhana seperti aslinya
#     grouped = df.groupby(group_cols).agg(
#         number_of_orders=('order_id', pd.Series.nunique),
#         number_of_sellers=('seller_id', pd.Series.nunique),
#         historical_cost=('price', 'median')
#     ).dropna().reset_index()

#     # Hindari pembagian dengan nol (persis seperti kode asli)
#     grouped['number_of_sellers'] = grouped['number_of_sellers'].replace(0, 1)

#     # Formula multiplier yang lebih dinamis tetapi tetap sederhana
#     # Menggunakan akar kuadrat untuk kurva respons yang lebih halus
#     demand_factor = np.sqrt(grouped['number_of_orders'])
#     supply_factor = np.sqrt(grouped['number_of_sellers'])
    
#     # Multiplier dengan range yang lebih luas
#     multiplier = (1 + 0.05 * demand_factor) / (1 + 0.05 * supply_factor)
#     multiplier = np.clip(multiplier, 0.8, 1.2)  # Range 30% diskon sampai 50% premium

#     # Hitung harga disesuaikan (struktur sama dengan asli)
#     grouped['adjusted_price'] = grouped['historical_cost'] * multiplier
#     grouped['price_multiplier'] = multiplier  # Tambahkan kolom multiplier untuk analisis
    
#     return grouped


# def calculate_dynamic_pricing(df, group_cols):
#     df['order_date'] = pd.to_datetime(df['order_purchase_timestamp']).dt.date

#     grouped = df.groupby(group_cols).agg(
#         number_of_orders=('order_id', 'count'),
#         number_of_sellers=('seller_id', 'count'),
#         historical_cost=('price', 'median')
#     ).dropna().reset_index()

#     # Hindari pembagian dengan nol
#     grouped['number_of_sellers'] = grouped['number_of_sellers'].replace(0, 1)

#     # Hitung multiplier dengan batas atas dan bawah
#     multiplier = (1 + 0.02 * grouped['number_of_orders']) / (1 + 0.02 * grouped['number_of_sellers'])
#     multiplier = np.clip(multiplier, 0.85, 1.3)  # Contoh: batas antara 85%–130%

#     grouped['adjusted_price'] = grouped['historical_cost'] * multiplier

#     return grouped

# def calculate_dynamic_pricing(df, group_cols):
#     df['order_date'] = pd.to_datetime(df['order_purchase_timestamp']).dt.date
#     grouped = df.groupby(group_cols).agg(
#         number_of_orders=('order_id', 'count'),
#         number_of_sellers=('seller_id', 'count'),
#         historical_cost=('price', 'median')
#     ).dropna().reset_index()

#     # Harga naik seiring order, turun seiring seller
#     grouped['adjusted_price'] = grouped['historical_cost'] * (
#         (1 + 0.02 * grouped['number_of_orders']) / (1 + 0.02 * grouped['number_of_sellers'])
#     )

#     return grouped

#versi lama

# def calculate_dynamic_pricing(df, group_cols):
#     # Pastikan tanggal sudah dalam format date
#     #df['order_date'] = pd.to_datetime(df['order_purchase_timestamp']).dt.date

#     # Grouping berdasarkan kolom yang ditentukan
#     grouped = df.groupby(group_cols).agg(
#         number_of_orders=('order_id', 'count'),
#         number_of_sellers=('seller_id', 'nunique'),
#         historical_cost=('price', 'mean')).dropna().reset_index()

#     # Percentile untuk multiplier
#     high_demand = np.percentile(grouped['number_of_orders'], 75)
#     low_demand = np.percentile(grouped['number_of_orders'], 25)

#     high_supply = np.percentile(grouped['number_of_sellers'], 75)
#     low_supply = np.percentile(grouped['number_of_sellers'], 25)

#     # Demand multiplier
#     grouped['demand_multiplier'] = np.where(
#         grouped['number_of_orders'] > high_demand,
#         grouped['number_of_orders'] / high_demand,
#         grouped['number_of_orders'] / low_demand)

#     # Supply multiplier
#     grouped['supply_multiplier'] = np.where(
#         grouped['number_of_sellers'] > high_supply, 
#         low_supply/ grouped['number_of_sellers'],
#         high_supply / grouped['number_of_sellers'])

#     # Threshold
#     demand_threshold_low = 0.5
#     supply_threshold_high = 0.5

#     # Adjusted price
#     cb_mlp = (
#         np.maximum(grouped['demand_multiplier'], demand_threshold_low) *
#         np.maximum(grouped['supply_multiplier'], supply_threshold_high))
    
#     # Batasi multiplier agar tidak lebih dari 1.3 (30% kenaikan maksimum)
#     max_increase = 1.15
#     final_multiplier = np.minimum(cb_mlp, max_increase)

#     # Hitung harga akhir dengan batas atas
#     grouped['adjusted_price'] = grouped['historical_cost'] * final_multiplier

#     return grouped



def get_dynamic_pricing(df, group_cols):
    return calculate_dynamic_pricing(df, group_cols)

def feature_engineering():
    """Performs feature engineering on the e-commerce transaction data."""
    os.makedirs('feature', exist_ok=True)
    df = pd.read_csv("data/e-commerce_transaction.csv")
    df_processed = calculate_dynamic_pricing(df.copy(), ['product_id', 'product_category_name', 'customer_state'])
    return df_processed

def get_dataframe():
    """Returns the processed dataframe."""
    return feature_engineering()

if __name__ == "__main__":
    df = pd.read_csv("data/e-commerce_transaction.csv") # Baca DataFrame di sini
    data = get_dynamic_pricing(df, ['product_id','product_category_name', 'customer_state'])
    print("Dynamic Pricing Data:")
    print(data.head(20))

    processed_df = feature_engineering()
    print("\nFeature engineering completed. Processed DataFrame:")
    print(processed_df.head())