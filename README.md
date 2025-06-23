# DA-Health-Inequality

미국 카운티별 건강 격차 분석 프로젝트

---

## 개요

이 프로젝트는 2025년 [County Health Rankings](https://www.countyhealthrankings.org/) 데이터를 기반으로 다음을 수행합니다:

- 건강 지표 및 조기사망률의 결측치 처리 및 전처리
- 인종별 건강 수준의 탐색적 분석 (EDA)
- 지도 기반 Choropleth 시각화
- KMeans 클러스터링 기반 군집 분석
- 클러스터별 건강 특성 요약 리포트 자동 생성

보건정책, 지역 격차 분석, 커뮤니티 건강 수준 평가를 위한 **데이터 기반 인사이트 생성 도구**로 활용할 수 있습니다.

---

## 기술 스택

| 영역              | 기술                                       |
| ----------------- | ------------------------------------------ |
| **언어**          | Python 3.9+                                |
| **데이터 처리**   | pandas, numpy                              |
| **시각화**        | matplotlib, seaborn                        |
| **지도 시각화**   | geopandas                                  |
| **모델링**        | scikit-learn (StandardScaler, KMeans, PCA) |
| **리포트 자동화** | csv 및 텍스트 리포트 생성                  |
| **실행 방식**     | 커맨드라인 기반 스크립트 실행 구조         |

---

## 프로젝트 구조

```
DA-Health-Inequality/
├── data/
│   ├── raw/                  # 원본 데이터 CSV
│   ├── external/             # Shapefile 등
│   └── processed/            # 전처리 완료된 CSV
│
├── output/
│   ├── clusters/             # 클러스터링 결과
│   ├── figures/
│   │   ├── eda/              # 결측, 분포, 상관관계, 인종별 비교
│   │   └── clusters/         # PCA 시각화, 클러스터 평균
│   ├── maps/                 # Choropleth 지도 결과
│   ├── reports/              # 자동 생성된 클러스터 리포트
│   └── tables/               # 수치 요약 테이블
│
├── src/
│   ├── eda/                  # EDA 분석 모듈
│   ├── modeling/             # 클러스터링 및 분석 로직
│   ├── report/               # 리포트 자동 생성 로직
│   ├── visualization/        # 시각화 함수 모음
│   └── utils/                # 데이터 전처리, 컬럼 관리 등
│
├── run_eda.py                # EDA 실행 진입점
├── run_modeling.py           # 클러스터링 실행 진입점
├── run_report.py             # 리포트 생성 실행
├── run_all.py                # 전체 실행 통합 스크립트
├── requirements.txt
└── README.md
```

---

## requirements.txt

```

pandas
matplotlib
seaborn
geopandas
scikit-learn

```

설치:

```bash
pip install -r requirements.txt
```

---

## 실행 방법

### 전체 실행

```bash
python run_all.py
```

### 단계별 실행

```bash
python run_eda.py         # EDA: 결측치, 분포, 상관, 인종별 그룹 비교
python run_modeling.py    # KMeans 클러스터링 + PCA 시각화
python run_report.py      # 클러스터 요약 리포트 자동 생성
```

---

## 주요 결과물

| 경로                                        | 내용                                |
| ------------------------------------------- | ----------------------------------- |
| `output/clusters/health_clusters.csv`       | 각 카운티별 클러스터 ID             |
| `output/figures/eda/`                       | 분포, 상관관계, 결측치 등 시각화    |
| `output/maps/map_Premature_Death_Total.png` | 카운티별 조기사망률 지도            |
| `output/reports/cluster_summary.txt`        | 클러스터 특성 요약 리포트           |
| `output/tables/correlation_table.csv`       | 인종별 사망률 vs 건강 지표 상관분석 |

---

## 기능 요약

- 데이터 전처리 및 결측치 보정
- 탐색적 분석: 수치 요약, 히스토그램, 상관 행렬 등
- 지도 기반 Choropleth 시각화 (GeoPandas)
- KMeans 클러스터링 → PCA 기반 시각화 포함
- 클러스터별 건강 특징 자동 요약 텍스트 리포트

---

## Contact

- **Email**: [sbeep2001@gmail.com](mailto:sbeep2001@gmail.com)
- **GitHub**: [github.com/CelestynPark](https://github.com/CelestynPark)