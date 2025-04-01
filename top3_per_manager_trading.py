import streamlit as st
import pandas as pd

data = [
    {"Manager": "Alpha Capital", "Stock": "NVIDIA", "End Wgt": 6.5, "Delta Wgt": 1.2},
    {"Manager": "Alpha Capital", "Stock": "Apple", "End Wgt": 5.8, "Delta Wgt": -0.4},
    {"Manager": "Alpha Capital", "Stock": "Microsoft", "End Wgt": 4.9, "Delta Wgt": 0.6},
    {"Manager": "Beta Partners", "Stock": "Tesla", "End Wgt": 7.1, "Delta Wgt": -1.1},
    {"Manager": "Beta Partners", "Stock": "Google", "End Wgt": 6.4, "Delta Wgt": 0.9},
    {"Manager": "Beta Partners", "Stock": "Meta", "End Wgt": 5.2, "Delta Wgt": 0.3},
    {"Manager": "Gamma Investments", "Stock": "AMD", "End Wgt": 8.3, "Delta Wgt": 2.0},
    {"Manager": "Gamma Investments", "Stock": "Intel", "End Wgt": 7.7, "Delta Wgt": -0.5},
    {"Manager": "Gamma Investments", "Stock": "Qualcomm", "End Wgt": 6.0, "Delta Wgt": 1.1},
]

df = pd.DataFrame(data)
df_sorted = df.sort_values(by=["Manager", "End Wgt"], ascending=[True, False])

def format_table(df):
    styled = df.style.format({
        "End Wgt": "{:.1f}%",
        "Delta Wgt": lambda x: f"{x:+.1f}%"
    })
    return styled

st.set_page_config(page_title="Top 3 Holdings by Manager", layout="wide")
st.markdown("## 🧮 Top 3 Holdings by Manager (Trading Effect)")
st.markdown("Showing each manager's top 3 holdings by % of portfolio and their weight change.")
st.dataframe(format_table(df_sorted), use_container_width=True)

st.markdown("---")
st.markdown("### 📊 Breakdown by Manager")
for mgr in df_sorted["Manager"].unique():
    st.markdown(f"#### {mgr}")
    mgr_df = df_sorted[df_sorted["Manager"] == mgr].copy()
    st.dataframe(format_table(mgr_df), use_container_width=True)
