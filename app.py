import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="자수 컬러 추천 시스템", layout="centered")

# 타이틀
st.markdown("""
<h1 style='text-align: center;'>🎨 자수 컬러 추천 시스템</h1>
<p style='text-align: center;'>원단 HEX 색상을 입력하면 미리 매핑된 자수 심색을 표시합니다.</p>
""", unsafe_allow_html=True)

# CSV 데이터 로드하기
def load_mapping():
    return pd.read_csv("fabric_to_thread_mapping.csv")

mapping_df = load_mapping()

# 색상 입력방
hex_input = st.text_input("원단 HEX 코드 입력 (예: #627A95)", value="")

if hex_input:
    hex_input = hex_input.upper()
    if not hex_input.startswith("#"):
        hex_input = f"#{hex_input}"

    match = mapping_df[mapping_df["Fabric HEX"] == hex_input]

    if not match.empty:
        row = match.iloc[0]
        fabric_hex = row["Fabric HEX"]
        thread_hex = row["Thread HEX"]
        thread_code = row["Thread Code"]

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 입력 원단 컬러")
            st.markdown(f"""
            <div style='width:150px;height:150px;background-color:{fabric_hex};border-radius:10px;display:flex;align-items:center;justify-content:center;border:1px solid #ccc;'>
                <span style='color:{thread_hex}; font-size:72px; font-family:sans-serif;'>h</span>
            </div>
            <p><strong>심 번호:</strong> {thread_code}</p>
            <p><strong>심 HEX:</strong> {thread_hex}</p>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("#### 추천 자수 컬러 (로고 색상)")
            st.markdown(f"""
            <div style='width:150px;height:150px;background-color:#ffffff;border-radius:10px;display:flex;align-items:center;justify-content:center;border:1px solid #ccc;'>
                <span style='color:{thread_hex}; font-size:72px; font-family:sans-serif;'>h</span>
            </div>
            """, unsafe_allow_html=True)

    else:
        st.warning("\u26a0\ufe0f 해당 원단 색상에 대한 매핑값이 없습니다.")
