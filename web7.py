import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========== BASIC PAGE CONFIG ==========
st.set_page_config(
    page_title="Dashboard Pertumbuhan Anak",
    page_icon="🍼",
    layout="wide"
)

# ========== DATA ==========
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

df = pd.DataFrame(
    data,
    columns=["No", "Usia (Tahun & Bulan)", "Tinggi (cm)", "Berat (kg)", "Lingkar Kepala (cm)"]
)

# ---------- HELPERS ----------
def usia_ke_bulan(usia_str: str) -> int:
    # asumsi format "X tahun Y bulan" / "X tahun" / "Y bulan"
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

# tambahkan kolom helper
df["Total Bulan"] = df["Usia (Tahun & Bulan)"].apply(usia_ke_bulan)
df["Kategori"]     = df["Total Bulan"].apply(kategori_usia)

# --- definisi sederhana stunting: ambang tinggi < WHO -2SD kira‑kira  ❗️
def stunting(row):
    if row["Kategori"] == "Bayi":   # <1 thn   ambang ±70 cm
        return row["Tinggi (cm)"] < 70
    elif row["Kategori"] == "Batita":  # 1‑3 thn ambang ±85 cm
        return row["Tinggi (cm)"] < 85
    else:                             # 3‑5 thn ambang ±95 cm
        return row["Tinggi (cm)"] < 95

df["Stunting"] = df.apply(stunting, axis=1)

# ========== SIDEBAR NAV ==========
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih halaman", ["Beranda", "Visualisasi"])

# ========= BERANDA =========
if page == "Beranda":
    st.title("🍼 Dashboard Pertumbuhan Anak")
    st.markdown(
        """
        Dashboard ini menampilkan ringkasan **pertumbuhan** dan **status stunting**
        untuk 23 anak dalam tiga kelompok usia:
        **Bayi (0–12 bln), Batita (1–3 thn), Balita (>3–5 thn)**.
        """
    )

    # ------- GLOBAL METRICS -------
    total_anak     = len(df)
    total_stunted  = int(df["Stunting"].sum())
    persen_stunted = total_stunted / total_anak

    g1, g2, g3 = st.columns([1,1,2])
    g1.metric("Total Anak", f"{total_anak}")
    g2.metric("Total Stunting", f"{total_stunted}",
              delta=f"{persen_stunted:.0%}")
    g3.markdown(
        f"""
        **Definisi singkat**  
        - *Stunting* 👉 tinggi < ambang WHO‑2SD (di‑aproksimasi: 70/85/95 cm per kategori)<br>
        - Warna &nbsp;<span style="color:#d11">🔴</span>&nbsp; di Visualisasi menandai anak stunting
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

    # ------- STATISTIK PER KATEGORI -------
    st.subheader("Statistik Tiap Kategori")

    for cat in ["Bayi", "Batita", "Balita"]:
        subset = df[df["Kategori"] == cat]
        n   = len(subset)
        ns  = int(subset["Stunting"].sum())
        rtg = subset["Tinggi (cm)"].mean()
        rtb = subset["Berat (kg)"].mean()

        with st.container():
            st.markdown(f"### {cat}")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Jumlah Anak", n)
            c2.metric("Stunting", f"{ns}", delta=f"{ns/n:.0%}")
            c3.metric("Tinggi Rata‑rata", f"{rtg:.1f} cm")
            c4.metric("Berat Rata‑rata", f"{rtb:.1f} kg")

            st.progress(ns/n if n else 0)
            # Penjelasan singkat
            st.caption(
                f"👉 Dari {n} {cat.lower()}, **{ns} anak ({ns/n:.0%})** "
                "terklasifikasi stunting berdasarkan ambang WHO yang disederhanakan."
            )
            st.markdown("---")

    st.info(
        "💡 *Interpretasi:* Persentase stunting **≥20 %** "
        "dianggap masalah kesehatan masyarakat serius menurut WHO."
    )

# ========== VISUALISASI ==========
elif page == "Visualisasi":
    st.title("📊 Visualisasi Pertumbuhan Anak")

    # Pilihan kategori usia
    kategori_pilihan = st.selectbox("Pilih Kategori Usia", ["Semua", "Bayi", "Batita", "Balita"])
    
    # Filter berdasarkan pilihan
    if kategori_pilihan != "Semua":
        data_viz = df[df["Kategori"] == kategori_pilihan]
    else:
        data_viz = df.copy()
    
    # Reset index agar grafik rapi
    data_viz = data_viz.reset_index(drop=True)

    # Grafik Tinggi Badan
    st.subheader("📏 Grafik Tinggi Badan Anak")
    fig1, ax1 = plt.subplots(figsize=(12, 5))
    sns.barplot(
        x=data_viz.index,
        y=data_viz["Tinggi (cm)"],
        hue=data_viz["Stunting"].map({True: "Stunting", False: "Normal"}),
        dodge=False,
        palette={"Stunting": "#e63946", "Normal": "#457b9d"},
        ax=ax1
    )
    ax1.set_xlabel("Anak ke-")
    ax1.set_ylabel("Tinggi (cm)")
    ax1.set_title(f"Tinggi Badan - Kategori: {kategori_pilihan}")
    st.pyplot(fig1)

    # Grafik Berat Badan
    st.subheader("⚖️ Grafik Berat Badan Anak")
    fig2, ax2 = plt.subplots(figsize=(12, 5))
    sns.barplot(
        x=data_viz.index,
        y=data_viz["Berat (kg)"],
        hue=data_viz["Stunting"].map({True: "Stunting", False: "Normal"}),
        dodge=False,
        palette={"Stunting": "#e63946", "Normal": "#457b9d"},
        ax=ax2
    )
    ax2.set_xlabel("Anak ke-")
    ax2.set_ylabel("Berat (kg)")
    ax2.set_title(f"Berat Badan - Kategori: {kategori_pilihan}")
    st.pyplot(fig2)

    # Tampilkan tabel data
    with st.expander("📋 Lihat Tabel Data"):
        st.dataframe(data_viz[["Usia (Tahun & Bulan)", "Kategori", "Tinggi (cm)", "Berat (kg)", "Stunting"]])

    # Tombol download CSV
    st.download_button(
        "⬇️ Download Data CSV",
        data_viz.to_csv(index=False).encode("utf-8"),
        file_name=f"data_{kategori_pilihan.lower()}.csv",
        mime="text/csv"
    )
