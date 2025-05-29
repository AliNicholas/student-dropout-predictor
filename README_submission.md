# Proyek Akhir: Prediksi Dropout Mahasiswa di Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan selama ini sukses mencetak banyak lulusan berkualitas. Namun, tingkat **dropout** yang relatif tinggi menjadi permasalahan serius, baik dari segi reputasi maupun finansial (biaya pendampingan dan rekrutmen ulang). Untuk mengurangi angka dropout, institut ingin **mendeteksi dini** mahasiswa berisiko sehingga dapat diberikan intervensi proaktif.

**Permasalahan Bisnis**  
- Tingginya angka dropout (>30% dari total mahasiswa)  
- Kurangnya visibility terhadap faktor penyebab utama dropout  
- Kebutuhan intervensi tepat waktu agar mahasiswa dapat diselamatkan dan dibiayai hingga lulus  

**Cakupan Proyek**  
1. Analisis data & preprocessing  
2. Visualisasi & Business Dashboard di Google Looker Studio  
3. Pengembangan Prototype ML (Streamlit + joblib)  
4. Rekomendasi Action Items  

**Sumber Data**  
Dataset “students_performance” dari Dicoding Academy:  
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md  

## Business Dashboard
Dashboard interaktif dibuat di Google Looker Studio dengan komponen utama:  
- **KPI Header**:  
  - Total Students: 4 424  
  - Total Graduates: 2 209  
  - Total Dropouts: 1 421  
  - Overall Dropout Rate: 32,12%  
- **Dropout Rate by Course**: bar chart vertikal menampilkan 10 course dengan rate tertinggi  
- **Dropout Rate by Application Mode**: bar chart per mode pendaftaran  
- **Graduate vs Dropout per Previous Qualification**: stacked column chart (Hijau = Graduate, Oranye = Dropout)  
- **Graduate vs Dropout per Attendance Mode**: stacked column chart (Pagi vs Malam)

**Link Dashboard**  
https://lookerstudio.google.com/reporting/c3a5439a-29d5-4109-b3e7-904ad0e6e6e7

## Prototype Machine Learning
Prototype aplikasi dibuat menggunakan Streamlit dan **model Gradient Boosting** yang disimpan di `model/gradientboosting_best.joblib`.

**Cara Menjalankan Lokal**  
1. Aktifkan virtual environment  
   - Windows: `venv\Scripts\activate`  
   - macOS/Linux: `source venv/bin/activate`  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Jalankan Streamlit:  
   ```bash
   streamlit run app.py
   ```

**Input Features**  
Admission Grade, Previous Qualification Grade, Curricular Units Grade (1st & 2nd sem), dsb.

**Output**  
Prediksi “Dropout” atau “Graduate” beserta confidence score.

**Link Prototype**  
(menyusul)

## Conclusion
- Model **Gradient Boosting** (best model) mencapai **ROC-AUC 0.953** dan **Accuracy ~91%**  
- Mahasiswa program malam dan lulusan previous qualification tertentu memiliki risiko dropout lebih tinggi  
- Admission grade & semester pass rate terbukti sebagai prediktor kuat

## Rekomendasi Action Items
1. **Early Warning System**: Integrasi model ke portal akademik untuk flag mahasiswa berisiko tinggi  
2. **Focused Mentoring**: Bimbingan khusus untuk mahasiswa evening attendance dan lulusan kualifikasi rendah  
3. **Academic Support**: Kursus tambahan atau tutoring pada semester pertama  
4. **Monitoring & Reporting**: Update dashboard bulanan, evaluasi efektivitas intervensi  
5. **Feedback Loop**: Survei mahasiswa berisiko untuk memahami kendala non-akademik seperti finansial atau kesehatan  

---

Jika Anda memerlukan plot atau analisis tambahan (misal heatmap korelasi, distribusi fitur lain), beri tahu saya dengan kode tertentu—saya akan menyiapkannya untuk Anda jalankan dan mengirim hasilnya.
