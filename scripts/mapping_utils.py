import pandas as pd
import numpy as np
from feature_engineering import get_dataframe
import os


data = get_dataframe()


""" DOCSTRING"""
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(data['product_id'])
org_label = le.classes_
enc_label = range(len(le.classes_))
product_id_map = dict(zip(org_label, enc_label))
data['product_id_enc'] = data['product_id'].map(product_id_map)


""" DOCSTRING"""
product_category = data['product_category_name']
customer_st = data['customer_state']
unique_info = data.drop_duplicates(subset='product_id')[['product_id', 'product_category_name', 'customer_state']]
product_info = dict(zip(unique_info['product_id'], zip(unique_info['product_category_name'], unique_info['customer_state'])))


""" DOCSTRING"""
merged = pd.DataFrame.from_dict(product_info, orient='index', columns = ['product_category_name','customer_state'])
merged.reset_index(inplace=True)
merged.rename(columns={'index':'product_id'}, inplace=True)



#Mapping
product_category_map = {
    'Agro_Industry_And_Commerce': 239.02153153153154,
    'Air_Conditioning': 193.12535031847133,
    'Art': 107.19664,
    'Arts_And_Craftmanship': 93.46312499999999,
    'Audio': 143.76246913580246,
    'Auto': 122.5136780104712,
    'Baby': 113.52516445470282,
    'Bed_Bath_Table': 131.15992125984252,
    'Books_General_Interest': 111.6870207253886,
    'Books_Imported': 93.25690476190476,
    'Books_Technical': 97.0312972972973,
    'Cds_Dvds_Musicals': 89.85818181818182,
    'Christmas_Supplies': 87.73022727272728,
    'Cine_Photo': 96.32039999999999,
    'Computers': 372.8123076923076,
    'Computers_Accessories': 143.16584360476864,
    'Consoles_Games': 128.69317415730336,
    'Construction_Tools_Construction': 162.26493256262043,
    'Construction_Tools_Lights': 150.27339869281045,
    'Construction_Tools_Safety': 190.50037037037038,
    'Cool_Stuff': 158.11517211328976,
    'Costruction_Tools_Garden': 138.8006,
    'Costruction_Tools_Tools': 122.91597222222224,
    'Diapers_And_Hygiene': 117.79666666666668,
    'Drinks': 96.81435555555555,
    'Dvds_Blu_Ray': 92.48772727272727,
    'Electronics': 74.20153387533874,
    'Fashio_Female_Clothing': 104.13740740740741,
    'Fashion_Bags_Accessories': 88.95949039881832,
    'Fashion_Childrens_Clothes': 94.505,
    'Fashion_Male_Clothing': 122.37438775510205,
    'Fashion_Shoes': 108.07952879581151,
    'Fashion_Sport': 107.37076923076924,
    'Fashion_Underwear_Beach': 89.8880412371134,
    'Fixed_Telephony': 134.28670967741934,
    'Flowers': 67.81227272727273,
    'Food': 86.62140186915889,
    'Food_Drink': 93.41389743589743,
    'Furniture_Bedroom': 107.33099999999999,
    'Furniture_Decor': 134.64923434856175,
    'Furniture_Living_Room': 139.56748691099477,
    'Furniture_Mattress_And_Upholstery': 174.99666666666667,
    'Garden_Tools': 138.54620881155128,
    'Health_Beauty': 138.93024947690327,
    'Home_Appliances': 93.16306640625,
    'Home_Appliances_2': 247.02578125,
    'Home_Comfort_2': 63.99117647058823,
    'Home_Confort': 175.11205323193917,
    'Home_Construction': 159.90168674698796,
    'Housewares': 108.5887441740031,
    'Industry_Commerce_And_Business': 182.48013157894738,
    'Kitchen_Dining_Laundry_Garden_Furniture': 126.37486238532111,
    'La_Cuisine': 230.185,
    'Luggage_Accessories': 115.49466386554622,
    'Market_Place': 112.79020942408377,
    'Music': 144.3904,
    'Musical_Instruments': 161.79696319018404,
    'Office_Furniture': 195.81420560747662,
    'Party_Supplies': 100.67730769230769,
    'Perfumery': 137.81338301716352,
    'Pet_Shop': 131.35940783986655,
    'Security_And_Services': 115.45,
    'Signaling_And_Security': 133.11123595505617,
    'Small_Appliances': 158.59928767123287,
    'Small_Appliances_Home_Oven_And_Coffee': 106.61157894736841,
    'Sports_Leisure': 129.3060853681984,
    'Stationery': 111.2574074074074,
    'Tablets_Printing_Image': 110.0141935483871,
    'Telephony': 80.41140955631398,
    'Toys': 129.28465544244324,
    'Watches_Gifts': 183.53816893878644
}


# Mapping ke kolom baru
data["product_category_enc"] = data["product_category_name"].map(product_category_map)

# Cek hasil
print(data[["product_category_name", "product_category_enc"]].head())

#Converting time of booking to a numerical feature
state_map = {
    "Andhra Pradesh": 0.685111306,
    "Gujarat": 0.130986103,
    "Chhattisgarh": 0.048393077,
    "Haryana": 0.030343928,
    "Delhi": 0.022854346,
    "Karnataka": 0.021386092,
    "Jammu & Kashmir": 0.010826523,
    "Madhya Pradesh": 0.008690881,
    "West Bengal": 0.008587065,
    "Arunachal Pradesh": 0.007489581,
    "Rajasthan": 0.005413262,
    "Maharashtra": 0.00504249,
    "Tamil Nadu": 0.004122977,
    "Himachal Pradesh": 0.004019161,
    "Kerala": 0.002476753,
    "Orissa": 0.001631394,
    "Uttar Pradesh": 0.001542409,
    "Punjab": 0.000548742,
    "Uttaranchal": 0.000533911
}

# Mapping ke dataframe
data["customer_state_enc"] = data["customer_state"].map(state_map)

# Cek hasil
print(data[["customer_state", "customer_state_enc"]].head())
