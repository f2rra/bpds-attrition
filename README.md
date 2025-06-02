# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding

Perusahaan Jaya Jaya Maju adalah sebuah perusahaan multinasional dengan jumlah karyawan lebih dari 1000 yang tersebar di seluruh penjuru negeri. Namun dalam beberapa tahun terakhir, perusahaan mengalami tantangan serius terkait tingginya _attrition rate_ atau keluarnya karyawan (>10%). Oleh karena itu, penting bagi manajemen HR untuk memahami akar penyebab dari attrition dan memiliki sistem yang mampu mengidentifikasi karyawan berisiko tinggi untuk keluar secara proaktif.

### Permasalahan Bisnis

Tingginya angka attrition berdampak langsung pada operasional dan strategi perusahaan, di antaranya:

**1. Meningkatnya biaya rekrutmen dan pelatihan ulang karyawan baru.**  
Proses mencari, mewawancarai, dan merekrut karyawan baru memerlukan investasi waktu dan sumber daya yang signifikan. Setelah direkrut, karyawan baru membutuhkan pelatihan untuk memahami peran mereka, budaya perusahaan, dan sistem internal, yang semuanya menambah biaya operasional.

**2. Mengganggu kontinuitas proyek dan stabilitas tim kerja.**  
Ketika karyawan penting keluar, proyek yang sedang berjalan dapat tertunda atau bahkan terhenti. Hilangnya pengetahuan institusional dan keahlian spesifik dapat menyebabkan penurunan produktivitas dan kualitas hasil kerja. Selain itu, dinamika tim dapat terganggu, menyebabkan demotivasi dan peningkatan beban kerja bagi karyawan yang tersisa.

**3. Melemahnya citra perusahaan sebagai pemberi kerja.**  
Tingginya _attrition rate_ dapat merusak reputasi perusahaan di mata calon karyawan dan juga publik. Perusahaan yang sering kehilangan karyawan bisa dianggap memiliki lingkungan kerja yang tidak baik, kurangnya peluang pengembangan, atau budaya perusahaan yang tidak mendukung. Ini membuat rekrutmen talenta baru menjadi lebih sulit dan mahal.

### Cakupan Proyek

1. Melakukan eksplorasi dan analisis data karyawan.
2. Mengidentifikasi faktor-faktor yang mempengaruhi attrition.
3. Membangun model klasifikasi untuk memprediksi risiko attrition.
4. Membuat business dashboard interaktif menggunakan Metabase untuk mendukung pengambilan keputusan HR.
5. Memberikan rekomendasi strategis untuk menurunkan tingkat attrition.

## Persiapan

### Sumber Data

Dataset yang digunakan bersumber dari: [employee_data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

### Instalasi & Setup

1. Buka terminal lalu clone repository ini:

   ```bash
   git clone https://github.com/f2rra/proyek-attrition.git
   cd proyek-attrition
   ```

   _Note: Siapkan Git sebelum menjalankan baris perintah di atas melalui terminal._

2. Buat environment dan install dependensi:

   ```bash
   conda create -n attrition-env python=3.11
   conda activate attrition-env
   pip install -r requirements.txt
   ```

   _Note: Install Anaconda atau Miniconda sebelum menjalankan baris perintah di atas melalui terminal._

### Menjalankan Skrip Prediksi

Untuk menjalankan prediksi attrition pada dataset baru:

1. Jalankan file `predict.py`

```bash
python predict.py
```

2. Masukkan data karyawan yang ingin diprediksi.
3. Hasil prediksi akan ditampilkan.

## Business Dashboard

Dashboard bisnis dikembangkan menggunakan Metabase dan berisi visualisasi interaktif mengenai faktor-faktor utama penyebab attrition.

### Akses Dashboard

Untuk mengakses dashboard:

1. Jalankan instance Metabase lokal.
2. Salin file `metabase.db.mv.db` ke folder Metabase default (biasanya `~/.metabase/`).
3. Login menggunakan:
   - **Email**: `admin@jayajayamaju.co.id`
   - **Password**: `admin123`

Jika dashboard dihosting secara publik, Anda juga dapat mengakses melalui:

> [Akses Dashboard (Public)](http://localhost:3000/public/dashboard/397c6fa4-40eb-496b-bb0b-6165cd6f749d)

**Catatan**: Pastikan sudah terhubung ke database internal atau file data karyawan yang digunakan.
