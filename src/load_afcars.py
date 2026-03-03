"""
Load AFCARS 2019 and 2020 from holistic/, filter to girls, write to data/processed/.

Run from project root:
  python -m src.load_afcars
  or
  python src/load_afcars.py

AFCARS SEX: 1 = Male, 2 = Female (per federal codebook). We keep SEX == 2.
"""
import pandas as pd
from pathlib import Path

# Paths (so script works when run as script or as module)
_ROOT = Path(__file__).resolve().parent.parent
HOLISTIC = _ROOT / "holistic"
PROCESSED = _ROOT / "data" / "processed"
AFCARS_2019_TAB = HOLISTIC / "afcars_2019" / "FC2019ABv1.tab"
AFCARS_2020_TAB = HOLISTIC / "afcars_2020" / "FC2020ABv1.tab"
AFCARS_2019_GIRLS = PROCESSED / "afcars_2019_girls.csv"
AFCARS_2020_GIRLS = PROCESSED / "afcars_2020_girls.csv"

# SEX: 1 = Male, 2 = Female (verify in holistic/afcars_2019/AFCARS FC Codebook.pdf)
SEX_FEMALE = 2


def load_afcars_year(path: Path) -> pd.DataFrame:
    """Load one AFCARS .tab file."""
    if not path.exists():
        raise FileNotFoundError(f"AFCARS file not found: {path}")
    return pd.read_csv(path, sep="\t", low_memory=False)


def filter_to_girls(df: pd.DataFrame, sex_col: str = "SEX") -> pd.DataFrame:
    """Keep only rows where child is female."""
    if sex_col not in df.columns:
        raise ValueError(f"Column {sex_col!r} not in dataframe. Columns: {list(df.columns)}")
    return df[df[sex_col].astype(int) == SEX_FEMALE].copy()


def main():
    PROCESSED.mkdir(parents=True, exist_ok=True)

    print("Loading AFCARS 2019 ...")
    df19 = load_afcars_year(AFCARS_2019_TAB)
    print(f"  Total rows: {len(df19):,}")

    print("Loading AFCARS 2020 ...")
    df20 = load_afcars_year(AFCARS_2020_TAB)
    print(f"  Total rows: {len(df20):,}")

    print("Filtering to girls (SEX == 2) ...")
    girls19 = filter_to_girls(df19)
    girls20 = filter_to_girls(df20)
    print(f"  2019 girls: {len(girls19):,}")
    print(f"  2020 girls: {len(girls20):,}")

    print(f"Writing to {PROCESSED} ...")
    girls19.to_csv(AFCARS_2019_GIRLS, index=False)
    girls20.to_csv(AFCARS_2020_GIRLS, index=False)
    print(f"  {AFCARS_2019_GIRLS.name}")
    print(f"  {AFCARS_2020_GIRLS.name}")
    print("Done. Next: link to NYTD Outcomes (holistic/nytd_outcomes_fy2020/Outcomes20_w3.tab).")


if __name__ == "__main__":
    main()
