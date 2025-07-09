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

with tabs[2]:
    st.header("변수별 관계 분석")

    st.markdown("""
        주요 사회경제 변수들과 건강 결과(Premature Death, Poor/Fair Health) 간의 관계를 시각화하였다.
        아래 그래프는 각 변수에 따라 건강 지표가 어떻게 변하는지를 보여준다.                
    """)

    scatter_plots = [
        ("아동 빈곤율과 조기 사망률", "Children_in_poverty_vs_premature_death_scatter.png"),
        ("고등학교 졸업률과 조기 사망률", "high_school_comletion_vs_premature_death_scatter.png"),
        ("실업률과 사망률", "unemployment_vs_premature_death_scatter.png"),
        ("빈곤율과 Poor/Fair Health", "poverty_vs_health_scatter.png"),
        ("영향도 분석 (Influence Plot)", "influence_plot.png"),
        ("정규성 검정 (QQ Plot)", "qq_plot.png"),
        ("규모-위치 플롯 (Scale-Location Plot)", "scale_location.png")
    ]

    for title, filename in scatter_plots:
        img_path = os.path.join("output", "figures", filename)
        if os.path.exists(img_path):
            st.image(img_path, caption=title)

with tabs[3]:
    st.header("클러스터링 시각화")

    st.markdown("""
        군집 기반 건강 격차 분석 결과를 지도 및 요약 통계로
    """)

    clustering_img_path = os.path.join("output", "maps", "map_Premature_Death_Total.png")
    if os.path.exists(clustering_img_path):
        st.image(clustering_img_path, caption="미국 카운티 클러스터링 지도 (사망률 기반)")

    if os.path.exists("output/reports/cluster_summary.txt"):
        st.subheader("클러스터 요역 통계")
        with open("output/reports/cluster_summary.txt", "r", encoding='utf-8') as f:
            summary = f.read()
            st.text(summary)
        st.text_area("Cluster Summary", summary, height=300)

