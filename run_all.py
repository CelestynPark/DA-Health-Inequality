import subprocess

if __name__ == '__main__':
    print("\n==== [1/3] EDA 실행 ====")
    subprocess.run(["python", "run_eda.py"])

    print("\n==== [2/3] Clustering Modeling 실행 ====")
    subprocess.run(["python", "run_modeling.py"])

    print("\n==== [3/3] Report 자동 생성 ====")
    subprocess.run(["python", "run_report.py"])