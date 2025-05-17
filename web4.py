import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Posyandu Lansia RW18",
    page_icon="🌿",
    layout="wide"
)

# ---------- Data Manual ----------
data = {
    "no": list(range(1, 31)),
    "Usia": [49, 59, 63, 60, 61, 61, 63, 57, 69, 58, 66, 57, 63, 60, 66, 63, 57, 66, 75, 56, 65, 63, 62, 60, 75, 63, 65, 63, 63, 63],
    "Tinggi": [147.5, 149, 52.4, 144.9, 151.5, 150, 152.7, 152.5, 155, 136.7, 152.7, 157, 158, 145.2, 146.5, 146.5, 151.6, 148.5, 147.6, 147.6, 146, 144, 144, 144.8, 156.5, 138.5, 147, 145.9, 150, 148.5],
    "Berat": [57.8, 52.4, 47.7, 42.4, 55.6, 69.8, 70.9, 56.2, 52.8, 45.5, 61.3, 60.7, 66.6, 41.6, 54.1, 55.6, 54.2, 50.3, 52.2, 52.8, 45.7, 45.7, 80.35, 46.7, 59.6, 45, 39.9, 46.2, 80.2, 54.2],
    "tekanan darah": ["138/82", "163/80", "155/71", "127/73", "174/87", "150/122", "152/80", "139/89", "165/88", "165/97", "167/83", "118/77", "155/82", "150/85", "161/93", "117/71", "157/96", "176/91", "153/80", "156/78", "125/73", "141/93", "139/69", "128/69", "152/93", "124/81", "109/76", "111/79", "170/102", "124/70"],
    "Lingkar Perut": [85, 83, 80, 81, 89, 89, 96, 86, 78, 84, 96, 96, 99, 71, 89, 78, 90, 85, 78, 82, 75, 93, 102, 81, 86, 84, 72, 82, 114, 86],
    "Gula Darah": [113, 134, 96, 178, 350, 357, 98, 111, 95, 169, 126, 159, 163, 109, 108, 111, 100, 145, 196, 107, 103, 109, 96, 188, 141, 87, 89, 94, 175, 121]
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
        "Analisis Tekanan & Gula Darah"
    ]
)

# ---------- Halaman Beranda ----------
if halaman == "Beranda":
    st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>📊 Dashboard Kesehatan Posyandu RW18</h1>
    <p style='text-align: center; font-size:18px;'>Selamat datang! Aplikasi ini menyajikan data pemeriksaan kesehatan warga RW18 secara interaktif dan informatif.</p>
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
    - Rata-rata Usia peserta adalah sekitar 62 tahun, menunjukkan mayoritas peserta adalah lansia.
    - Tinggi dan Berat rata-rata menunjukkan komposisi tubuh yang bervariasi.
    - Beberapa nilai Gula Darah sangat Tinggi, menunjukkan risiko diabetes yang perlu perhatian lebih lanjut.
    - Tekanan darah rata-rata menunjukkan banyak peserta berada di kategori pre-hipertensi hingga hipertensi.
    """)

# ---------- Halaman Data Lengkap ----------
elif halaman == "Data Lengkap":
    st.markdown("## 📋 Data Lengkap Pemeriksaan")
    st.dataframe(df, use_container_width=True)

# ---------- Statistik ----------
elif halaman == "Statistik":
    st.markdown("## 📊 Statistik")
    kolom_numerik = ["Usia", "Tinggi", "Berat", "Lingkar Perut", "Gula Darah"]
    statistik_df = pd.DataFrame({
        "Rata-rata": df[kolom_numerik].mean(),
        "Median": df[kolom_numerik].median(),
        "Modus": df[kolom_numerik].mode().iloc[0]
    }).round(2)

    st.dataframe(statistik_df, use_container_width=True)

# ---------- Visualisasi ----------
elif halaman == "Visualisasi":
    st.markdown("## 📈 Visualisasi Data")
    pilihan = st.selectbox("Pilih data yang ingin divisualisasikan:", ["Usia", "Tinggi", "Berat", "Lingkar Perut", "Gula Darah", "Tekanan Darah Sistolik", "Tekanan Darah Diastolik"])
    st.bar_chart(df[pilihan])

    if pilihan in ["Gula Darah", "Berat"]:
        st.line_chart(df[pilihan])

# ---------- Pembahasan Tekanan Darah ----------
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

# ---------- Pembahasan Gula Darah ----------
elif halaman == "Pembahasan Gula Darah":
    st.markdown("## 🩸 Pembahasan Gula Darah")
    st.markdown("""
    ### Kategori Gula Darah (mg/dL):
    - **Rendah**: < 70
    - **Normal**: 70 – 99
    - **Pre-diabetes**: 100 – 125
    - **Diabetes**: ≥ 126
    """)

# ---------- Analisis Tekanan & Gula Darah ----------
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
    - Mayoritas warga memiliki tekanan darah **Pre-hipertensi dan Hipertensi Tahap 1**, menunjukkan kecenderungan tekanan darah Tinggi.
    - Untuk Gula Darah, sebagian besar masuk kategori **Pre-diabetes dan Diabetes**, menandakan potensi risiko diabetes.
    - Rekomendasi: edukasi, pemeriksaan rutin, dan promosi gaya hidup sehat sangat diperlukan.
    """)

# ---------- Footer ----------
st.markdown("""
<hr style='border:1px solid #ccc;'>
<p style='text-align: center; color: grey;'>© 2025 Digitalisasi Hasil Posyandu Lansia RW18 | KKN PPM UGM 2025 PERIODE 1 </p>
""", unsafe_allow_html=True)
