import streamlit as st
from PIL import Image
import os

st.set_page_config(layout="wide")
st.title("County Health Inequality Dashboard")

tabs = st.tabs([
    '프로젝트 개요',
    '회귀 분석 결과',
    '변수별 관계 분석',
    '클러스트링 시각화'
])

with tabs[0]:
    st.header("프로젝트 개요")
    st.markdown("""
        본 프로젝트는 미국 카운티별 건강 불평등 요인을 분석하고,
        사회경제적 변수들이 사망률(Premature Death) 및 건강 지표(Poor/Fair Health)에 어떤 영향을 주는지를 분석한다.
        
        - 데이터 출처: [County Health Rankings & Roadmaps](http://www.countyhealthranking.org/)
        - 주요 분석:
             -회귀 분석
             -다중공산성 분석 (VIF)
             -변수별 시각화
             -클러스터링
""")

with tabs[1]:
    st.header("회귀 계수 및 진단 결과")

    coef_path = os.path.join("output", "figures", "socioeconomic_coefficients.png")
    diag_path = os.path.join("output", "figures", "residuals_vs_fitted.png")

    if os.path.exists(coef_path):
        st.image(coef_path, caption="회귀 계수 (Regression Coefficients)")

    if os.path.exists(diag_path):
        st.image(diag_path, caption="잔차 대 적합값 (Residuals vs Fitted)")