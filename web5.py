import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Posyandu Lansia RW19",
    page_icon="🌿",
    layout="wide"
)

# ---------- Data Manual ----------
data = {
    "no": list(range(1, 33)),
    "Usia": [55, 75, 72, 75, 60, 65, 61, 65, 69, 60, 58, 61, 90, 70, 60, 56, 71, 65, 74, 72, 65, 94, 70, 74, 60, 85, 70, 70, 83, 80, 65, 60],
    "Tinggi": [149.0, 146.5, 142.8, 159.5, 156.7, 150.4, 149.7, 143.2, 143.2, 153.6, 158.0, 146.0, 150.0, 159.5, 150.3, 138.7, 145.4, 147.4, 146.0, 144.6, 135.5, 146.4, 154.2, 163.3, 143.5, 140.0, 145.0, 140.0, 162.0, 145.0, 141.3, 147.0],
    "Berat": [61, 50.55, 79, 58, 70.8, 47.2, 39.75, 43.4, 49.8, 62.7, 55.2, 47.4, 46.35, 65.3, 51.7, 30.4, 50.85, 45.2, 58.65, 46.05, 42.9, 53.95, 40.25, 47.15, 80.5, 43.8, 36.85, 47.2, 51.4, 48.95, 40.95, 39.95],
    "tekanan darah": ["162/96", "186/88", "110/79", "141/89", "181/100", "169/93", "134/79", "123/66", "164/101", "128/71", "165/102", "164/107", "154/88", "112/81", "123/79", "150/103", "176/101", "152/78", "129/81", "140/91", "191/81", "155/80", "164/93", "148/98", "198/106", "175/87", "156/97", "221/96", "143/81", "164/98", "105/66", "163/86"],
    "Lingkar Perut": [101, 96, 66, 84, 95, 90, 63, 88, 88, 97, 81, 79, 93, 88, 79, 86, 93, 89, 99, 86, 88, 100, 70, 89, 110, 85, 78, 99, 87, 95, 87, 87],
    "Gula Darah": [91, 97, 110, 131, 100, 133, 98, 192, 89, 133, 96, 106, 106, 134, 96, 107, 117, 135, 114, 110, 186, 191, 110, 92, 114, 104, 183, 127, 102, 128, 121, 116],
    "Asam Urat": [5.2, 5.3, 6.3, 5.5, 5.3, 7.4, 3.4, 5, 5, 5.3, 5.8, 4.9, 6.1, 7.3, 4.7, 4.5, 6, 7.5, 4.3, 4.5, 8.4, 7.2, 8.6, 6.7, 6.6, 5.2, 3.8, 4.8, 6.1, 7.9, 3.3, 5.7]
}

df = pd.DataFrame(data)
bp_split = df["tekanan darah"].str.split("/", expand=True).astype(int)
bp_split.columns = ["Tekanan Darah Sistolik", "Tekanan Darah Diastolik"]
df = pd.concat([df, bp_split], axis=1)

# ---------- Sidebar ----------
st.sidebar.title("🌿 Navigasi")
halaman = st.sidebar.selectbox(
    "Pilih Halaman",
    [
        "Beranda",
        "Data Lengkap",
        "Statistik",
        "Visualisasi",
        "Pembahasan Tekanan Darah",
        "Pembahasan Gula Darah",
        "Pembahasan Asam Urat",
        "Analisis Tekanan & Gula Darah"
    ]
)

# ---------- Halaman Beranda ----------
if halaman == "Beranda":
    st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>📊 Dashboard Kesehatan Posyandu RW19</h1>
    <p style='text-align: center; font-size:18px;'>Selamat datang! Aplikasi ini menyajikan data pemeriksaan kesehatan warga RW19 secara interaktif dan informatif.</p>
    <hr style='border:1px solid #2E8B57;'>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("👵 Rata-rata Usia", f"{df['Usia'].mean():.1f} tahun")
    col2.metric("📏 Rata-rata Tinggi", f"{df['Tinggi'].mean():.1f} cm")
    col3.metric("⚖️ Rata-rata Berat", f"{df['Berat'].mean():.1f} kg")

    col4, col5, col6 = st.columns(3)
    col4.metric("🩺 Rata-rata Tekanan Darah Sistolik", f"{df['Tekanan Darah Sistolik'].mean():.0f} mmHg")
    col5.metric("🩺 Rata-rata Tekanan Darah Diastolik", f"{df['Tekanan Darah Diastolik'].mean():.0f} mmHg")
    col6.metric("🩸 Rata-rata Gula Darah", f"{df['Gula Darah'].mean():.0f} mg/dL")

    st.markdown("""
    ### 📌 Penjelasan Statistik Sederhana
    Dari data yang ditampilkan:
    - Rata-rata Usia peserta adalah sekitar 69 tahun, menunjukkan mayoritas peserta adalah lansia.
    - Beberapa nilai Gula Darah sangat Tinggi, menunjukkan risiko diabetes.
    - Tekanan darah rata-rata menunjukkan banyak peserta berada di kategori pre-hipertensi hingga hipertensi.
    - Asam Urat Tinggi juga terdeteksi pada sebagian warga, yang berisiko menyebabkan gout.
    """)

elif halaman == "Data Lengkap":
    st.markdown("## 📋 Data Lengkap Pemeriksaan")
    st.dataframe(df, use_container_width=True)

elif halaman == "Statistik":
    st.markdown("## 📊 Statistik")
    kolom_numerik = ["Usia", "Tinggi", "Berat", "Lingkar Perut", "Gula Darah", "Asam Urat"]
    statistik_df = pd.DataFrame({
        "Rata-rata": df[kolom_numerik].mean(),
        "Median": df[kolom_numerik].median(),
        "Modus": df[kolom_numerik].mode().iloc[0]
    }).round(2)
    st.dataframe(statistik_df, use_container_width=True)

elif halaman == "Visualisasi":
    st.markdown("## 📈 Visualisasi Data")
    pilihan = st.selectbox("Pilih data yang ingin divisualisasikan:", ["Usia", "Tinggi", "Berat", "Lingkar Perut", "Gula Darah", "Asam Urat", "Tekanan Darah Sistolik", "Tekanan Darah Diastolik"])
    st.bar_chart(df[pilihan])
    if pilihan in ["Gula Darah", "Berat", "Asam Urat"]:
        st.line_chart(df[pilihan])

elif halaman == "Pembahasan Tekanan Darah":
    st.markdown("## 🩺 Pembahasan Tekanan Darah")
    st.markdown("""
    ### Kategori Tekanan Darah (mmHg):
    - **Normal**: Tekanan Darah Sistolik < 120 dan Tekanan Darah Diastolik < 80
    - **Pre-hipertensi**: Tekanan Darah Sistolik 120–139 atau Tekanan Darah Diastolik 80–89
    - **Hipertensi Tahap 1**: Tekanan Darah Sistolik 140–159 atau Tekanan Darah Diastolik 90–99
    - **Hipertensi Tahap 2**: Tekanan Darah Sistolik ≥ 160 atau Tekanan Darah Diastolik ≥ 100
    - **Hipotensi**: Tekanan Darah Sistolik < 90 atau Tekanan Darah Diastolik < 60
    """)

elif halaman == "Pembahasan Gula Darah":
    st.markdown("## 🩸 Pembahasan Gula Darah")
    st.markdown("""
    ### Kategori Gula Darah (mg/dL):
    - **Rendah**: < 70
    - **Normal**: 70 – 99
    - **Pre-diabetes**: 100 – 125
    - **Diabetes**: ≥ 126
    """)

elif halaman == "Pembahasan Asam Urat":
    st.markdown("## ⚠️ Pembahasan Asam Urat")
    st.markdown("""
    ### Kategori Umum Asam Urat (mg/dL):
    - **Normal (Pria)**: 3.4 – 7.0
    - **Normal (Wanita)**: 2.4 – 6.0
    - **Tinggi**: > 7.0 (berisiko gout)
    - **Rendah**: < 3.4
    """)
    def kategori_asam_urat(val):
        if val < 3.4:
            return "Rendah"
        elif val > 7.0:
            return "Tinggi"
        else:
            return "Normal"
    df["Kategori Asam Urat"] = df["Asam Urat"].apply(kategori_asam_urat)
    count_asam = df["Kategori Asam Urat"].value_counts()
    st.subheader("📈 Distribusi Kategori Asam Urat")
    st.dataframe(count_asam.rename("Jumlah"))
    st.bar_chart(count_asam)

elif halaman == "Analisis Tekanan & Gula Darah":
    st.markdown("## 📉 Analisis Tekanan Darah dan Gula Darah")
    def kategori_tekanan(s, d):
        if s < 90 or d < 60:
            return "Hipotensi"
        elif s < 120 and d < 80:
            return "Normal"
        elif 120 <= s <= 139 or 80 <= d <= 89:
            return "Pre-hipertensi"
        elif 140 <= s <= 159 or 90 <= d <= 99:
            return "Hipertensi Tahap 1"
        else:
            return "Hipertensi Tahap 2"
    def kategori_gula(g):
        if g < 70:
            return "Rendah"
        elif g <= 99:
            return "Normal"
        elif g <= 125:
            return "Pre-diabetes"
        else:
            return "Diabetes"
    df["Kategori Tekanan Darah"] = df.apply(lambda row: kategori_tekanan(row["Tekanan Darah Sistolik"], row["Tekanan Darah Diastolik"]), axis=1)
    df["Kategori Gula Darah"] = df["Gula Darah"].apply(kategori_gula)
    tekanan_count = df["Kategori Tekanan Darah"].value_counts()
    gula_count = df["Kategori Gula Darah"].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🩺 Distribusi Tekanan Darah")
        st.dataframe(tekanan_count.rename("Jumlah"))
        st.bar_chart(tekanan_count)
    with col2:
        st.subheader("🩸 Distribusi Gula Darah")
        st.dataframe(gula_count.rename("Jumlah"))
        st.bar_chart(gula_count)
    st.markdown("""
    ### 📌 Kesimpulan Analisis
    - Mayoritas warga memiliki tekanan darah **Pre-hipertensi dan Hipertensi Tahap 1**.
    - Sebagian besar Gula Darah menunjukkan kecenderungan **Pre-diabetes dan Diabetes**.
    - Edukasi, skrining rutin, dan promosi gaya hidup sehat sangat dianjurkan.
    """)

st.markdown("""
<hr style='border:1px solid #ccc;'>
<p style='text-align: center; color: grey;'>© 2025 Digitalisasi Hasil Posyandu Lansia RW19 | KKN PPM UGM 2025 PERIODE 1 </p>
""", unsafe_allow_html=True)
