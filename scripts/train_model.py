#backup training_model.py

import pandas as pd
import numpy as np
import psycopg2
from sqlalchemy import create_engine, text, URL
from urllib.parse import quote_plus
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest, f_regression, mutual_info_regression
from sklearn.model_selection import train_test_split
import mapping_utils as mapping_utils
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from joblib import load, dump
data= mapping_utils.data
merged = mapping_utils.merged


"""Train Split&Test"""

# Train model
print("Training model...")

def train_model(data):
  x = data[['product_id_enc', 'product_category_enc', 'customer_state_enc','historical_cost','number_of_orders']]
  y = data['adjusted_price']
  x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state=42)
  rf = RandomForestRegressor()
  rf.fit(x_train, y_train)
  return rf

model = train_model(data)

# Simpan model ke file
print("Saving model...")
# with open('models/randomforest.pkl', 'wb') as f:
#   pickle.dump(model, f)
# print("Model saved.")



# #Compress model
# print("Compressing model...")
# model = load('models/randomforest.pkl')  # Memuat model lama
dump(model, 'models/randomforest_compressed.pkl', compress=3)  # Simpan dengan kompresi
print("Model Compressed.")


#function untuk memprediksi harga


def product_category_numeric(product_category_enc):
  product_category_numeric_mapping = mapping_utils.product_category_map
  product_category_numeric = product_category_numeric_mapping.get(product_category_enc)
  return product_category_numeric

def state_numeric(customer_state_enc):
  state_numeric_mapping = mapping_utils.state_map
  state_numeric = state_numeric_mapping.get(customer_state_enc)
  return state_numeric

def product_id_numeric(product_id_enc):
  product_id_numeric_mapping = mapping_utils.product_id_map
  product_id_numeric = product_id_numeric_mapping.get(product_id_enc)
  return product_id_numeric

#user Input baru
def predict_price(product_id_enc,product_category_enc,customer_state_enc,historical_cost,number_of_orders):

  product_id_numeric_result = product_id_numeric(product_id_enc)
  if product_id_enc not in merged['product_id'].values:
    raise ValueError("Invalid Product Id")

  product_category_numeric_result = product_category_numeric(product_category_enc)
  checking_one = merged[merged['product_id'] == product_id_enc]
  if product_category_enc not in checking_one['product_category_name'].values:
    raise ValueError("Invalid Product Category")

  customer_state_numeric_result = state_numeric(customer_state_enc)
  checking_two = checking_one[checking_one['product_category_name'] == product_category_enc]
  if customer_state_enc not in checking_two['customer_state'].values:
    raise ValueError("Invalid Customer State ")
  
'''
    @st.cache_resource
    def train_model(data):
        x = data[['product_id_enc', 'product_category_enc', 'customer_state_enc','historical_cost','number_of_orders']]
        y = data['adjusted_price']
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state=42)
        rf = RandomForestRegressor()
        rf.fit(x_train, y_train)
        return rf
    '''