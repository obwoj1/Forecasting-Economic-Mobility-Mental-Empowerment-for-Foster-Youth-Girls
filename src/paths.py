"""Project paths. Use these so all code points at the same places."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
HOLISTIC = PROJECT_ROOT / "holistic"
PROCESSED = PROJECT_ROOT / "data" / "processed"
OUTPUTS = PROJECT_ROOT / "outputs"

# AFCARS (read from holistic)
AFCARS_2019_TAB = HOLISTIC / "afcars_2019" / "FC2019ABv1.tab"
AFCARS_2020_TAB = HOLISTIC / "afcars_2020" / "FC2020ABv1.tab"

# Processed outputs (written by pipelines)
AFCARS_2019_GIRLS = PROCESSED / "afcars_2019_girls.csv"
AFCARS_2020_GIRLS = PROCESSED / "afcars_2020_girls.csv"
