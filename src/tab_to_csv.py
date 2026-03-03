"""
Convert analysis .tab files to CSV for use in pipelines.
Run from project root: python src/tab_to_csv.py
Reads from holistic/ and writes CSV next to each .tab there.
"""
import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
HOLISTIC = PROJECT_ROOT / "holistic"

# (path to .tab relative to HOLISTIC, path to .csv relative to same folder)
FILES = [
    ("afcars_2019/FC2019ABv1.tab", "afcars_2019/FC2019ABv1.csv"),
    ("afcars_2020/FC2020ABv1.tab", "afcars_2020/FC2020ABv1.csv"),
    ("nytd_outcomes_fy2020/Outcomes20_w3.tab", "nytd_outcomes_fy2020/Outcomes20_w3.csv"),
    ("nytd_services/Services2023.tab", "nytd_services/Services2023.csv"),
]


def main():
    for tab_rel, csv_rel in FILES:
        tab_path = HOLISTIC / tab_rel
        csv_path = HOLISTIC / csv_rel
        if not tab_path.exists():
            print(f"Skip (not found): {tab_path}")
            continue
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        print(f"Reading {tab_path.name} ...")
        df = pd.read_csv(tab_path, sep="\t", low_memory=False)
        print(f"  rows={len(df):,} cols={len(df.columns)}")
        print(f"Writing {csv_path.name} ...")
        df.to_csv(csv_path, index=False)
        print(f"  done: {csv_path}")
    print("All conversions done.")


if __name__ == "__main__":
    main()
