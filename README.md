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

1. Siapkan Docker Desktop yang sudah terinstall.
1. Jalankan instance Metabase lokal.
1. Salin file `metabase.db.mv.db` ke folder Metabase default (biasanya `~/.metabase/`).
1. Login menggunakan:
   - **Email**: `admin@jayajayamaju.co.id`
   - **Password**: `admin123`

Jika dashboard dihosting secara publik, Anda juga dapat mengakses melalui:

> [Akses Dashboard (Public)](http://localhost:3000/public/dashboard/397c6fa4-40eb-496b-bb0b-6165cd6f749d)

**Catatan**: Pastikan sudah terhubung ke database internal atau file data karyawan yang digunakan.

## Conclusion

Berdasarkan analisis data dan model klasifikasi yang dikembangkan, beberapa faktor yang paling mempengaruhi attrition di Jaya Jaya Maju antara lain:

- Pendapatan bulanan yang relatif lebih kecil dibandingkan rata-rata.
- Karyawan yang sering bekerja lembur (OverTime).
- Work life balance yang rendah dari karyawan.
- Kurangnya pelatihan kerja (training times last year).
- Masa kerja yang pendek dan kurangnya promosi.

Selain itu berdasarkan proporsi data karyawan di dashboard, karyawan dengan ciri berikut lebih rentan mengalami attrition:

- Usia karyawan yang relatif muda (<22,5 tahun)
- Karyawan yang berperan sebagai sales representative.
- Karyawan dengan keterlibatan kerja rendah.
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

**3. Perkuat Program Pelatihan dan Pengembangan Karyawan (Training and Development):**

- Aksi: Tingkatkan frekuensi dan kualitas program pelatihan, khususnya yang relevan dengan kebutuhan peran dan pengembangan karir. Identifikasi kebutuhan pelatihan spesifik untuk berbagai kelompok karyawan, termasuk karyawan muda dan yang baru bergabung.
- Target: Meningkatkan kompetensi, rasa percaya diri, dan loyalitas karyawan karena merasa perusahaan berinvestasi pada mereka.

**4. Kembangkan Jalur Karier yang Jelas dan Program Retensi Terstruktur:**

- Aksi: Buat dan sosialisasikan jalur karier yang transparan dengan kriteria promosi yang jelas dan objektif. Implementasikan program retensi yang berfokus pada karyawan dengan masa kerja pendek (<5 tahun) dan karyawan muda, misalnya melalui program mentoring, rotasi pekerjaan untuk pengembangan, atau pengakuan atas pencapaian.
- Target: Meningkatkan motivasi, mengurangi attrition akibat stagnasi karir, dan mempertahankan talenta muda.

**5. Tingkatkan Keterlibatan Karyawan (Employee Engagement) dan Perhatian Khusus pada Kelompok Rentan:**

- Aksi: Lakukan survei keterlibatan secara berkala untuk memahami kebutuhan dan kekhawatiran karyawan. Kembangkan program untuk meningkatkan keterlibatan, seperti kegiatan tim, forum komunikasi terbuka, dan program pengakuan. Berikan perhatian khusus pada kelompok yang teridentifikasi rentan (Sales Representative, karyawan muda, karyawan dengan keterlibatan rendah, karyawan lajang) dengan program yang disesuaikan, misalnya dukungan manajerial yang lebih intensif atau komunitas internal.
- Target: Menciptakan lingkungan kerja yang lebih positif dan suportif, meningkatkan rasa memiliki, dan mengurangi attrition pada kelompok-kelompok spesifik.

**6. Implementasikan Mekanisme Feedback dan Monitoring Berkelanjutan:**

- Aksi: Gunakan business dashboard yang telah dibuat untuk secara aktif memonitor faktor-faktor penyebab attrition. Selain itu, adakan sesi exit interview yang mendalam untuk mendapatkan insight kualitatif dan sesi stay interview untuk karyawan yang masih aktif guna mengidentifikasi potensi masalah secara proaktif.
- Target: Memastikan strategi yang diimplementasikan efektif dan dapat disesuaikan seiring waktu berdasarkan data dan umpan balik terbaru.

Dengan mengimplementasikan rekomendasi-rekomendasi ini secara strategis dan berkelanjutan, Jaya Jaya Maju diharapkan dapat secara signifikan mengurangi attrition rate dan membangun lingkungan kerja yang lebih produktif serta mendukung pertumbuhan jangka panjang perusahaan.
