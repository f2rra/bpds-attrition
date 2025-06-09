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
   git clone https://github.com/f2rra/bpds-attrition.git
   cd bpds-attrition
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

1. Siapkan Docker Desktop yang sudah terinstall.
2. Jalankan docker compose.

```bash
docker compose up -d
```

3. Buka browser dan akses https://localhost:3000 lalu login menggunakan:
   - **Email**: `root@mail.com`
   - **Password**: `root123`

## Conclusion

Berdasarkan analisis data dan model klasifikasi yang dikembangkan, beberapa faktor yang paling mempengaruhi attrition di Jaya Jaya Maju antara lain:

- Pendapatan bulanan yang relatif lebih kecil dibandingkan rata-rata.
- Karyawan yang sering bekerja lembur (OverTime).
- Work life balance yang rendah dari karyawan.
- Masa kerja yang pendek.

Selain itu berdasarkan proporsi data karyawan di dashboard, karyawan dengan ciri berikut lebih rentan mengalami attrition:

- Usia karyawan yang relatif muda.
- Karyawan yang berperan sebagai sales representative.
- Karyawan dengan masa kerja di perusahaan kurang dari 5 tahun.
- Karyawan denagn status pernikahan lajang atau single.
- Karyawan yang lebih sering mengadakan perjalanan bisnis.

Model prediksi yang dibangun mampu membantu manajemen untuk mengidentifikasi karyawan dengan risiko keluar lebih dini.

### Rekomendasi Action Items

Berdasarkan temuan di atas, berikut adalah beberapa rekomendasi tindakan strategis yang dapat dipertimbangkan oleh Jaya Jaya Maju untuk menekan attrition rate dan meningkatkan retensi karyawan:

**1. Tinjau Ulang Struktur Gaji dan Tunjangan (Compensation and Benefits Review):**

- Aksi: Lakukan benchmarking gaji dengan standar industri dan kompetitor untuk memastikan kompensasi yang ditawarkan kompetitif, terutama untuk peran dengan attrition rate tinggi (seperti Sales Representative) dan karyawan dengan pendapatan di bawah rata-rata.
- Target: Mengurangi attrition yang disebabkan oleh ketidakpuasan finansial.

**2. Optimalisasi Beban Kerja dan Peningkatan Keseimbangan Kerja-Hidup (Work-Life Balance):**

- Aksi: Implementasikan kebijakan untuk mengurangi lembur berlebih, seperti penjadwalan yang lebih baik, redistribusi beban kerja, atau eksplorasi teknologi untuk efisiensi. Pertimbangkan program dukungan work-life balance (misalnya, fleksibilitas jam kerja, opsi kerja jarak jauh jika memungkinkan, cuti tambahan berdasarkan kinerja/masa kerja), terutama bagi karyawan yang sering lembur dan sering melakukan perjalanan bisnis.
- Target: Mengurangi stres dan kelelahan (burnout), meningkatkan kepuasan, dan menurunkan attrition akibat ketidakseimbangan kerja-hidup.

**3. Implementasikan Mekanisme Feedback dan Monitoring Berkelanjutan:**

- Aksi: Gunakan business dashboard yang telah dibuat untuk secara aktif memonitor faktor-faktor penyebab attrition. Selain itu, adakan sesi exit interview yang mendalam untuk mendapatkan insight kualitatif dan sesi stay interview untuk karyawan yang masih aktif guna mengidentifikasi potensi masalah secara proaktif.
- Target: Memastikan strategi yang diimplementasikan efektif dan dapat disesuaikan seiring waktu berdasarkan data dan umpan balik terbaru.

Dengan mengimplementasikan rekomendasi-rekomendasi ini secara strategis dan berkelanjutan, Jaya Jaya Maju diharapkan dapat secara signifikan mengurangi attrition rate dan membangun lingkungan kerja yang lebih produktif serta mendukung pertumbuhan jangka panjang perusahaan.
