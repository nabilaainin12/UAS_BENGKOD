# Customer Churn Prediction

Aplikasi prediksi churn pelanggan menggunakan algoritma Machine Learning untuk memprediksi apakah pelanggan akan berhenti menggunakan layanan (churn) atau tetap menggunakan layanan.

## Deskripsi Proyek

Proyek ini dibuat sebagai Ujian Akhir Semester (UAS) mata kuliah Bengkel Koding Data Science.

Dataset yang digunakan adalah **Sales and Marketing Customer Dataset** dari Kaggle.

## Dataset

Dataset:
https://www.kaggle.com/datasets/bhaskerpaul/sales-and-marketing-dataset

Jumlah data: **15.000 records**

Target:

- **0** = Tidak Churn
- **1** = Churn

## Tahapan Proyek

1. Exploratory Data Analysis (EDA)
2. Direct Modeling
3. Modeling dengan Preprocessing
4. Feature Selection
5. Hyperparameter Tuning
6. Evaluasi Model
7. Deployment menggunakan Streamlit Cloud

## Model Machine Learning

Model terbaik yang digunakan:

- **Random Forest Classifier**

Model diperoleh melalui proses:

- Feature Selection
- Hyperparameter Tuning menggunakan GridSearchCV

## Fitur Input

Aplikasi menggunakan 9 fitur terbaik hasil Feature Selection:

1. Total Spent
2. Satisfaction Score
3. Support Tickets
4. Marketing Spend Per User
5. Average Session Time
6. Lifetime Value
7. Membership Days
8. Average Order Value
9. Pages Per Session

## Cara Menjalankan Aplikasi Secara Lokal

### 1. Clone Repository

```bash
git clone https://github.com/username/customer-churn-prediction.git
```

### 2. Masuk ke Folder Proyek

```bash
cd customer-churn-prediction
```

### 3. Install Library

```bash
pip install -r requirements.txt
```

### 4. Jalankan Streamlit

```bash
streamlit run app.py
```

## Library yang Digunakan

- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn

## Deployment

Aplikasi dideploy menggunakan **Streamlit Cloud**.

## Author

Nama: **Nabila Ainin**

Mata Kuliah: **Bengkel Koding Data Science**

Universitas: **(Isi sesuai universitas Anda)**