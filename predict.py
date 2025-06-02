from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
import pandas as pd
import pickle

# Load encoder dan model yang sudah dilatih
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('onehot_encoder.pkl', 'rb') as encoder_file:
    encoder = pickle.load(encoder_file)

with open('ordinal_encoder.pkl', 'rb') as ordinal_encoder_file:
    ordinal_encoder = pickle.load(ordinal_encoder_file)
  
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

age = input("Masukkan usia karyawan: ")
business_travel = input("Masukkan jenis perjalanan bisnis (Travel_Rarely, Travel_Frequently, Non-Travel): ")
daily_rate = input("Masukkan Daily Rate: ")
department = input("Masukkan departemen (Sales, Research & Development, Human Resources): ")
distance_from_home = input("Masukkan jarak dari rumah (DistanceFromHome): ")
education = input("Masukkan tingkat pendidikan (1-5): ")
education_field = input("Masukkan bidang pendidikan (Life Sciences, Medical, Marketing, Technical Degree, Other): ")
environment_satisfaction = input("Masukkan kepuasan lingkungan kerja (1-4): ")
gender = input("Masukkan jenis kelamin (Male, Female): ")
hourly_rate = input("Masukkan Hourly Rate: ")
job_involvement = input("Masukkan tingkat keterlibatan pekerjaan (1-4): ")
job_level = input("Masukkan level pekerjaan (1-5): ")
job_role = input("Masukkan peran pekerjaan (Sales Executive, Research Scientist, Laboratory Technician, Manufacturing Director, Healthcare Representative, Manager, Sales Representative): ")
job_satisfaction = input("Masukkan kepuasan kerja (1-4): ")
marital_status = input("Masukkan status pernikahan (Single, Married, Divorced): ")
monthly_income = input("Masukkan pendapatan bulanan: ")
monthly_rate = input("Masukkan Monthly Rate: ")
num_companies_worked = input("Masukkan jumlah perusahaan yang pernah bekerja: ")
overtime = input("Masukkan apakah bekerja lembur (Yes, No): ")
percent_salary_hike = input("Masukkan persentase kenaikan gaji: ")
performance_rating = input("Masukkan rating kinerja (1-4): ")
relationship_satisfaction = input("Masukkan kepuasan hubungan kerja (1-4): ")
stock_option_level = input("Masukkan level opsi saham (0-3): ")
total_working_years = input("Masukkan total tahun bekerja: ")
training_times_last_year = input("Masukkan jumlah pelatihan tahun lalu: ")
work_life_balance = input("Masukkan keseimbangan kerja-hidup (1-4): ")
years_at_company = input("Masukkan tahun di perusahaan saat ini: ")
years_in_current_role = input("Masukkan tahun di peran saat ini: ")
years_since_last_promotion = input("Masukkan tahun sejak promosi terakhir: ")
years_with_curr_manager = input("Masukkan tahun dengan manajer saat ini: ")


# Masukkan data yang ingin diprediksi
X_new = pd.DataFrame({
    # Untuk pengisian data, anda bisa mengisi sesuai dengan data yang ingin diprediksi.
    # Contoh data yang bisa digunakan:
    # 'Age': [35],
    # 'BusinessTravel': ['Travel_Rarely'],
    # 'DailyRate': [1100],
    # 'Department': ['Sales'],
    # 'DistanceFromHome': [5],
    # 'Education': [3],
    # 'EducationField': ['Life Sciences'],
    # 'EnvironmentSatisfaction': [3],
    # 'Gender': ['Male'],
    # 'HourlyRate': [70],
    # 'JobInvolvement': [3],
    # 'JobLevel': [2],
    # 'JobRole': ['Sales Executive'],
    # 'JobSatisfaction': [4],
    # 'MaritalStatus': ['Single'],
    # 'MonthlyIncome': [5000],
    # 'MonthlyRate': [13000],
    # 'NumCompaniesWorked': [1],
    # 'OverTime': ['No'],
    # 'PercentSalaryHike': [12],
    # 'PerformanceRating': [3],
    # 'RelationshipSatisfaction': [4],
    # 'StockOptionLevel': [1],
    # 'TotalWorkingYears': [10],
    # 'TrainingTimesLastYear': [3],
    # 'WorkLifeBalance': [3],
    # 'YearsAtCompany': [5],
    # 'YearsInCurrentRole': [2],
    # 'YearsSinceLastPromotion': [1],
    # 'YearsWithCurrManager': [3],
    'Age': [int(age)],
    'BusinessTravel': [business_travel],
    'DailyRate': [int(daily_rate)],
    'Department': [department],
    'DistanceFromHome': [int(distance_from_home)],
    'Education': [int(education)],
    'EducationField': [education_field],
    'EnvironmentSatisfaction': [int(environment_satisfaction)],
    'Gender': [gender],
    'HourlyRate': [int(hourly_rate)],
    'JobInvolvement': [int(job_involvement)],
    'JobLevel': [int(job_level)],
    'JobRole': [job_role],
    'JobSatisfaction': [int(job_satisfaction)],
    'MaritalStatus': [marital_status],
    'MonthlyIncome': [int(monthly_income)],
    'MonthlyRate': [int(monthly_rate)],
    'NumCompaniesWorked': [int(num_companies_worked)],
    'OverTime': [overtime],
    'PercentSalaryHike': [int(percent_salary_hike)],
    'PerformanceRating': [int(performance_rating)],
    'RelationshipSatisfaction': [int(relationship_satisfaction)],
    'StockOptionLevel': [int(stock_option_level)],
    'TotalWorkingYears': [int(total_working_years)],
    'TrainingTimesLastYear': [int(training_times_last_year)],
    'WorkLifeBalance': [int(work_life_balance)],
    'YearsAtCompany': [int(years_at_company)],
    'YearsInCurrentRole': [int(years_in_current_role)],
    'YearsSinceLastPromotion': [int(years_since_last_promotion)],
    'YearsWithCurrManager': [int(years_with_curr_manager)],
})

# Mapping untuk Gender dan OverTime
X_new['Gender'] = X_new['Gender'].map({'Male': 0, 'Female': 1})
X_new['OverTime'] = X_new['OverTime'].map({'No': 0, 'Yes': 1})

# Ordinal Encoding untuk BusinessTravel
X_new['BusinessTravel'] = ordinal_encoder.transform(X_new[['BusinessTravel']])

# Kolom kategorikal yang tersisa untuk one-hot encoding
cat_cols_to_onehot = ['Department', 'EducationField', 'JobRole', 'MaritalStatus']

# One-Hot Encoding untuk sisa kolom kategorikal
encoded_data = encoder.transform(X_new[cat_cols_to_onehot])
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(cat_cols_to_onehot))
X_new = pd.concat([X_new.drop(columns=cat_cols_to_onehot), encoded_df], axis=1)

# Scaling data numerik
cols_to_scale = X_new.select_dtypes(exclude=['object', 'bool']).columns.tolist()
X_new[cols_to_scale] = scaler.transform(X_new[cols_to_scale])

# Lakukan prediksi pada data baru
y_pred_new = model.predict(X_new)

if y_pred_new[0] == 1:
    print("Karyawan ini berpotensi untuk keluar dari perusahaan.")
else:
    print("Karyawan ini tidak berpotensi untuk keluar dari perusahaan.")