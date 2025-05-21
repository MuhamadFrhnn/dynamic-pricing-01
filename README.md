Proyek ini menerapkan model penetapan harga dinamis (dynamic pricing) menggunakan machine learning berdasarkan data historis. Model diaplikasikan pada web web Streamlit. Model ini dapat memprediksi harga yang optimal berdasarkan fitur produk yang dapat digunakan untuk membantu pengambilan keputusan dalam strategi penetapan harga di bidang e-commerce.

Fitur Utama
- Upload dan pratinjau data
- Prediksi harga optimal menggunakan model
- Visualisasi performa harga
- Antarmuka interaktif berbasis Streamlit

________________________________________Final Model Testing 
Deskripsi
Model Dynamic Pricing yang telah dilatih dan diuji menggunakan Random Forest Regressor yang telah dilatih. Tujuan dari pengujian ini adalah untuk mengukur seberapa baik model dapat menggeneralisasi terhadap data baru dan memberikan prediksi yang akurat.
Langkah-Langkah
1.	Model Random Forest Regressor diterapkan untuk memprediksi harga yang akan di uji
2.	Prediksi dibandingkan dengan nilai aktualnya.
3.	Metrik evaluasi dihitung untuk menilai performa model.
________________________________________
 Link Aplikasi
Kunjungi aplikasi dynamic pricing:
https://dynamic-pricing-e-commerce.streamlit.app/ 

________________________________________
#  Dynamic Pricing E-Commerce

Proyek ini menerapkan model **penetapan harga dinamis (dynamic pricing)** menggunakan machine learning berdasarkan data historis. Model diaplikasikan pada web menggunakan Streamlit. Model ini dapat memprediksi harga yang optimal berdasarkan fitur produk yang dapat membantu pengambilan keputusan dalam strategi penetapan harga di bidang **e-commerce**.

---

## Struktur Direktori

```
├── scripts/
│   ├──__init__.py         
│   ├── feature_engineering.py                 
│   ├── mapping_utils.py            
│   └── test_connection.py              
│
├── venv/
│   ├──Lib/site-packages/pip         
│   ├──Scripts         
│   └──- pyvenv.cfg           
│
├── .gitignore
|
├── LICENSE                    
│
└── README.md                  
├── requirements.txt           
|
├── streamlit_app.py 

## Fitur Utama

-  Upload dan pratinjau data  
-  Prediksi harga optimal menggunakan model  
-  Visualisasi performa harga  
-  Antarmuka interaktif berbasis Streamlit  

## Petunjuk Penggunaan

### 1. Clone Repository

```bash
git clone https://github.com/MuhamadFrhnn/dynamic-pricing
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi Streamlit

```bash
streamlit run app.py
```

## Fitur-fitur yang Digunakan

Model Dynamic Pricing menggunakan fitur-fitur berikut:

1. **Product Category**
2. **Demand**
3. **Historical Price**
4. **Sales Volume**

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama
- **Pandas & NumPy**: Anaisis data
- **Scikit-learn**: Model machine learning
- **Matplotlib & Seaborn**: Visualisasi 
- **Streamlit**: membuat aplikasi web yang interaktif

## Pengembangan Lanjutan

Beberapa ide untuk pengembangan aplikasi selanjutnya:

1.	Implementasi model lain seerti XGBoost
2.	Diintegrasikan dengan dashboard e-commerce realtime
3.	Simulasi harga berdasarkan skenario pasar

## Kontributor

- Muhamad Farhan Haidar - Main Contributor
- Kahfi Sabillah Arfan - Second Contributor
- Azhari Dwi Pramesti - Second Contributor

## Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file LICENSE untuk detail.


