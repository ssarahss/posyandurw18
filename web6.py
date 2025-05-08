import streamlit as st
import pandas as pd
import numpy as np

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Posyandu RW18",
    page_icon="🌿",
    layout="wide"
)

# ---------- Data Manual for Dataset 1 ----------
data1 = {
    "no": list(range(1, 31)),
    "usia": [49, 59, 63, 60, 61, 61, 63, 57, 69, 58, 66, 57, 63, 60, 66, 63, 57, 66, 75, 56, 65, 63, 62, 60, 75, 63, 65, 63, 63, 63],
    "tinggi": [147.5, 149, 52.4, 144.9, 151.5, 150, 152.7, 152.5, 155, 136.7, 152.7, 157, 158, 145.2, 146.5, 146.5, 151.6, 148.5, 147.6, 147.6, 146, 144, 144, 144.8, 156.5, 138.5, 147, 145.9, 150, 148.5],
    "berat": [57.8, 52.4, 47.7, 42.4, 55.6, 69.8, 70.9, 56.2, 52.8, 45.5, 61.3, 60.7, 66.6, 41.6, 54.1, 55.6, 54.2, 50.3, 52.2, 52.8, 45.7, 45.7, 80.35, 46.7, 59.6, 45, 39.9, 46.2, 80.2, 54.2],
    "tekanan darah": ["138/82", "163/80", "155/71", "127/73", "174/87", "150/122", "152/80", "139/89", "165/88", "165/97", "167/83", "118/77", "155/82", "150/85", "161/93", "117/71", "157/96", "176/91", "153/80", "156/78", "125/73", "141/93", "139/69", "128/69", "152/93", "124/81", "109/76", "111/79", "170/102", "124/70"],
    "lingkar perut": [85, 83, 80, 81, 89, 89, 96, 86, 78, 84, 96, 96, 99, 71, 89, 78, 90, 85, 78, 82, 75, 93, 102, 81, 86, 84, 72, 82, 114, 86],
    "gula darah": [113, 134, 96, 178, 350, 357, 98, 111, 95, 169, 126, 159, 163, 109, 108, 111, 100, 145, 196, 107, 103, 109, 96, 188, 141, 87, 89, 94, 175, 121]
}

df1 = pd.DataFrame(data1)
bp_split1 = df1["tekanan darah"].str.split("/", expand=True).astype(int)
bp_split1.columns = ["Sistolik", "Diastolik"]
df1 = pd.concat([df1, bp_split1], axis=1)

# ---------- Data Manual for Dataset 2 ----------
data2 = {
    "no": list(range(1, 33)),
    "usia": [55, 75, 72, 75, 60, 65, 61, 65, 69, 60, 58, 61, 90, 70, 60, 56, 71, 65, 74, 72, 65, 94, 70, 74, 60, 85, 70, 70, 83, 80, 65, 60],
    "tinggi": [149.0, 146.5, 142.8, 159.5, 156.7, 150.4, 149.7, 143.2, 143.2, 153.6, 158.0, 146.0, 150.0, 159.5, 150.3, 138.7, 145.4, 147.4, 146.0, 144.6, 135.5, 146.4, 154.2, 163.3, 143.5, 140.0, 145.0, 140.0, 162.0, 145.0, 141.3, 147.0],
    "berat": [61, 50.55, 79, 58, 70.8, 47.2, 39.75, 43.4, 49.8, 62.7, 55.2, 47.4, 46.35, 65.3, 51.7, 30.4, 50.85, 45.2, 58.65, 46.05, 42.9, 53.95, 40.25, 47.15, 80.5, 43.8, 36.85, 47.2, 51.4, 48.95, 40.95, 39.95],
    "tekanan darah": ["162/96", "186/88", "110/79", "141/89", "181/100", "169/93", "134/79", "123/66", "164/101", "128/71", "165/102", "164/107", "154/88", "112/81", "123/79", "150/103", "176/101", "152/78", "129/81", "140/91", "191/81", "155/80", "164/93", "148/98", "198/106", "175/87", "156/97", "221/96", "143/81", "164/98", "105/66", "163/86"],
    "lingkar perut": [101, 96, 66, 84, 95, 90, 63, 88, 88, 97, 81, 79, 93, 88, 79, 86, 93, 89, 99, 86, 88, 100, 70, 89, 110, 85, 78, 99, 87, 95, 87, 87],
    "gula darah": [91, 97, 110, 131, 100, 133, 98, 192, 89, 133, 96, 106, 106, 134, 96, 107, 117, 135, 114, 110, 186, 191, 110, 92, 114, 104, 183, 127, 102, 128, 121, 116],
    "asam urat": [5.2, 5.3, 6.3, 5.5, 5.3, 7.4, 3.4, 5, 5, 5.3, 5.8, 4.9, 6.1, 7.3, 4.7, 4.5, 6, 7.5, 4.3, 4.5, 8.4, 7.2, 8.6, 6.7, 6.6, 5.2, 3.8, 4.8, 6.1, 7.9, 3.3, 5.7]
}

df2 = pd.DataFrame(data2)
bp_split2 = df2["tekanan darah"].str.split("/", expand=True).astype(int)
bp_split2.columns = ["Sistolik", "Diastolik"]
df2 = pd.concat([df2, bp_split2], axis=1)

# ---------- Sidebar Navigation ----------
st.sidebar.title("🌿 Navigasi")
dataset = st.sidebar.selectbox("Pilih Dataset", ["Dataset 1", "Dataset 2"])
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

# Set the dataset based on the selection
if dataset == "Dataset 1":
    df = df1
else:
    df = df2

# ---------- Handle the selected page ----------
if halaman == "Statistik":
    st.markdown("## 📊 Statistik Ringkasan")
    kolom_numerik = ["usia", "tinggi", "berat", "lingkar perut", "gula darah", "asam urat"]
    statistik_df = pd.DataFrame({
        "Rata-rata": df[kolom_numerik].mean(),
        "Median": df[kolom_numerik].median(),
        "Modus": df[kolom_numerik].mode().iloc[0]
    }).round(2)

    st.dataframe(statistik_df, use_container_width=True)

elif halaman == "Visualisasi":
    st.markdown("## 📈 Visualisasi Data")
    pilihan = st.selectbox("Pilih data yang ingin divisualisasikan:", ["usia", "tinggi", "berat", "lingkar perut", "gula darah", "Sistolik", "Diastolik", "asam urat"])
    st.bar_chart(df[pilihan])

    if pilihan in ["gula darah", "berat"]:
        st.line_chart(df[pilihan])

elif halaman == "Pembahasan Tekanan Darah":
    st.markdown("## 🩺 Pembahasan Tekanan Darah")
    st.markdown("""
    ### Kategori Tekanan Darah (mmHg):
    - **Normal**: Sistolik < 120 dan Diastolik < 80
    - **Pre-hipertensi**: Sistolik 120–139 atau Diastolik 80–89
    - **Hipertensi Tahap 1**: Sistolik 140–159 atau Diastolik 90–99
    - **Hipertensi Tahap 2**: Sistolik ≥ 160 atau Diastolik ≥ 100
    - **Hipotensi**: Sistolik < 90 atau Diastolik < 60
    """)

elif halaman == "Pembahasan Gula Darah":
    st.markdown("## 🩸 Pembahasan Gula Darah")
    st.markdown("""
    ### Kategori Gula Darah Puasa (mg/dL):
    - **Rendah**: < 70
    - **Normal**: 70 – 99
    - **Pre-diabetes**: 100 – 125
    - **Diabetes**: ≥ 126
    """)

elif halaman == "Pembahasan Asam Urat":
    st.markdown("## 🩺 Pembahasan Asam Urat")
    st.markdown("""
    ### Kategori Asam Urat (mg/dL):
    - **Normal**: 3.5 – 7.2
    - **Tinggi**: > 7.2
    """)

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

    def kategori_asam_urat(a):
        if a > 7.2:
            return "Tinggi"
        else:
            return "Normal"

    df["Kategori Tekanan Darah"] = df.apply(lambda row: kategori_tekanan(row["Sistolik"], row["Diastolik"]), axis=1)
    df["Kategori Gula Darah"] = df["gula darah"]
