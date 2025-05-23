import streamlit as st
import pandas as pd
import numpy as np


# ========== CONFIG ========== #
st.set_page_config(
    page_title="Dashboard Hasil Posyandu Anak RW 18",
    page_icon="🍼",
    layout="wide"
)

# ========== DATA ========== #
data = [
    [1, '2 tahun 7 bulan', 91, 12.55, 47],
    [2, '0 tahun 10 bulan', 72, 8.61, 45],
    [3, '5 tahun 1 bulan', 103, 15.3, 49.5],
    [4, '4 tahun 0 bulan', 99, 13.85, 48],
    [5, '1 tahun 8 bulan', 83, 10.45, 48.5],
    [6, '0 tahun 8 bulan', 67, 7.4, 43.5],
    [7, '3 tahun 6 bulan', 95, 12.65, 47],
    [8, '1 tahun 0 bulan', 80, 6.46, 45],
    [9, '3 tahun 0 bulan', 96, 14.9, 49.5],
    [10, '2 tahun 6 bulan', 93, 13.1, 48],
    [11, '5 tahun 0 bulan', 100, 13.7, 49],
    [12, '2 tahun 6 bulan', 90, 11.25, 46],
    [13, '0 tahun 3 bulan', 58, 5.2, 39],
    [14, '4 tahun 0 bulan', 102.3, 15.55, 51.5],
    [15, '2 tahun 0 bulan', 84.5, 9.35, 46.5],
    [16, '2 tahun 0 bulan', 99.8, 19.8, 49.7],
    [17, '3 tahun 0 bulan', 98.7, 15.5, 48.2],
    [18, '2 tahun 0 bulan', 85.5, 13.2, 48],
    [19, '2 tahun 8 bulan', 85.5, 10.65, 47],
    [20, '3 tahun 0 bulan', 90.5, 11.6, 50],
    [21, '2 tahun 4 bulan', 81, 11.9, 44],
    [22, '0 tahun 11 bulan', 76, 8.45, 44],
    [23, '3 tahun 2 bulan', 91, 11.55, 46.5],
]

df = pd.DataFrame(data, columns=["No", "Usia (Tahun & Bulan)", "Tinggi (cm)", "Berat (kg)", "Lingkar Kepala (cm)"])

# ========== HELPER FUNCTIONS ========== #
def usia_ke_bulan(usia_str: str) -> int:
    th, bl = 0, 0
    if "tahun" in usia_str:
        parts = usia_str.split("tahun")
        th = int(parts[0].strip())
        if "bulan" in parts[1]:
            bl = int(parts[1].replace("bulan", "").strip())
    else:
        bl = int(usia_str.replace("bulan", "").strip())
    return th * 12 + bl

def kategori_usia(total_bulan: int) -> str:
    if total_bulan <= 12:
        return "Bayi"
    elif total_bulan <= 36:
        return "Batita"
    else:
        return "Balita"

df["Total Bulan"] = df["Usia (Tahun & Bulan)"].apply(usia_ke_bulan)
df["Kategori"] = df["Total Bulan"].apply(kategori_usia)

# ========== SIDEBAR NAV ========== #
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih halaman", ["Beranda", "Visualisasi"])

# ========== BERANDA ========== #
if page == "Beranda":
    st.markdown("""
    <h1 style='text-align: center; color: #2E8B57;'>🍼 Dashboard Hasil Posyandu Anak RW18</h1>
    <p style='text-align: center; font-size:18px;'>Selamat datang! Aplikasi ini menyajikan data pertumbuhan anak berdasarkan usia, tinggi badan, berat badan, dan lingkar kepala secara interaktif dan informatif.</p>
    <hr style='border:1px solid #2E8B57;'>
    """, unsafe_allow_html=True)

    # Overall Metrics
    col1, col2 = st.columns(2)
    col1.metric("👶 Total Anak", f"{len(df)}")
    col2.metric("📊 Kategori Usia", f"{df['Kategori'].nunique()}")

    st.markdown("---")
    st.subheader("📌 Statistik Pertumbuhan per Kategori Usia")

    for cat in ["Bayi", "Batita", "Balita"]:
        subset = df[df["Kategori"] == cat]
        n = len(subset)
        rtg = subset["Tinggi (cm)"].mean()
        rtb = subset["Berat (kg)"].mean()
        rlk = subset["Lingkar Kepala (cm)"].mean()

        with st.container():
            st.markdown(f"### {cat}")
            c1, c2, c3 = st.columns(3)
            c1.metric("Jumlah Anak", n)
            c2.metric("Tinggi Rata-rata", f"{rtg:.1f} cm")
            c3.metric("Berat Rata-rata", f"{rtb:.1f} kg")
            st.metric("Lingkar Kepala Rata-rata", f"{rlk:.1f} cm")
            st.markdown("---")

# ========== VISUALISASI ========== #
elif page == "Visualisasi":
    st.title("📊 Visualisasi Pertumbuhan Anak")

    kategori_pilihan = st.selectbox("Pilih Kategori Usia", ["Semua", "Bayi", "Batita", "Balita"])

    data_viz = df if kategori_pilihan == "Semua" else df[df["Kategori"] == kategori_pilihan]
    data_viz = data_viz.reset_index(drop=True)

    # Grafik Tinggi Badan
    st.subheader("📏 Grafik Tinggi Badan Anak")
    tinggi_chart = pd.DataFrame({
        "Anak ke-": data_viz.index + 1,
        "Tinggi (cm)": data_viz["Tinggi (cm)"].to_numpy()
    })
    st.bar_chart(tinggi_chart.set_index("Anak ke-"))

    # Grafik Berat Badan
    st.subheader("⚖️ Grafik Berat Badan Anak")
    berat_chart = pd.DataFrame({
        "Anak ke-": data_viz.index + 1,
        "Berat (kg)": data_viz["Berat (kg)"].to_numpy()
    })
    st.bar_chart(berat_chart.set_index("Anak ke-"))

    # Tabel Data
    with st.expander("📋 Lihat Tabel Data"):
        st.dataframe(data_viz[["Usia (Tahun & Bulan)", "Kategori", "Tinggi (cm)", "Berat (kg)", "Lingkar Kepala (cm)"]])

    st.download_button(
        "⬇️ Download Data CSV",
        data_viz.to_csv(index=False).encode("utf-8"),
        file_name=f"data_{kategori_pilihan.lower()}.csv",
        mime="text/csv"
    )
