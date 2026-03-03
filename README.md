# Forecasting Economic Mobility & Mental Empowerment for Foster Youth Girls

**Authors:** Oba
**Term:** Spring 2025

## Overview

Foster youth girls face significant barriers to long-term success in education, employment, and mental health. This project builds a **predictive software system** using machine learning to forecast economic mobility and mental empowerment outcomes from socioeconomic and environmental signals.

## Approach

- **Data:** Public and agency datasets (CSV and other formats)
- **Methods:** Python data pipelines, supervised learning, optional explainable AI (interpretability focus)
- **Ethics:** Interpretability and ethical data sourcing emphasized from the start

## Repository structure

```
ur2phd/
├── holistic/           # Analysis data only: AFCARS, NYTD (.tab + codebooks), README, project plan
├── data/               # data/raw (placeholder), data/processed (pipelines write here)
├── notebooks/         # Exploratory analysis and experiments
├── src/               # Pipelines, models, utilities (e.g. tab_to_csv.py reads holistic/)
├── docs/              # Data rundown, cleanup record, proposal, implementation docs
├── outputs/           # Model outputs, figures, reports
├── requirements.txt
└── README.md
```

**Analysis data:** All inputs live in **`holistic/`** (see `holistic/README.md` and `holistic/PROJECT_PLAN_AND_STEPS.md`). Pipelines read from `holistic/` and write to `data/processed/` and `outputs/`.

## Setup

1. Clone the repo and enter the project directory.
2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Data

- **Analysis inputs:** `holistic/` — AFCARS and NYTD `.tab` files plus codebooks (see `holistic/README.md`).
- **Processed outputs:** Pipelines write cleaned/linked data to `data/processed/` and results to `outputs/`.

## Usage

1. **Setup:** `pip install -r requirements.txt` (from project root).
2. **Phase 1 — AFCARS (girls only):**  
   From project root run:  
   `python -m src.load_afcars`  
   This loads AFCARS 2019 and 2020 from `holistic/`, filters to girls (SEX == 2), and writes `data/processed/afcars_2019_girls.csv` and `afcars_2020_girls.csv`.
3. **Notebook:** Open `notebooks/01_load_afcars_girls.ipynb` and run (with kernel cwd = project root) to run the same pipeline and inspect the result.
4. **Next:** Link to NYTD Outcomes (`holistic/nytd_outcomes_fy2020/Outcomes20_w3.tab`) using state and youth IDs, then build models (see `holistic/` and `docs/` for the full plan).

## References

- Rosholm et al. (2024). Predictive risk modeling for child maltreatment detection and enhanced decision-making: Evidence from Danish administrative data. *PLOS ONE*, 19(7):e0305974.


