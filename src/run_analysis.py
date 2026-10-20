
import json
from pathlib import Path

import pandas as pd

from analysis import analyze_student_data


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "student-mat.csv"
RESULTS_DIR = PROJECT_ROOT / "results"


def main():
    # Load the dataset without changing the original file.
    data = pd.read_csv(DATA_PATH, sep=";")

    # Count records excluded for missing or invalid primary variables.
    required = ["studytime", "G3"]
    total_records = len(data)

    numeric = data[required].apply(pd.to_numeric, errors="coerce")
    valid = (
        numeric["studytime"].between(1, 4)
        & numeric["G3"].between(0, 20)
    )

    excluded_records = int((~valid).sum())
    clean_data = numeric.loc[valid].copy()

    # Run the preregistered statistical analysis.
    analysis_results = analyze_student_data(clean_data)

    results = {
        "dataset": "UCI Student Performance - Mathematics",
        "dataset_file": "data/student-mat.csv",
        "total_records": total_records,
        "valid_records": len(clean_data),
        "excluded_records": excluded_records,
        "exclusion_rule": (
            "Exclude records with missing or invalid studytime or G3."
        ),
        "analysis": analysis_results,
    }

    # Convert results into JSON-compatible values.
    results["analysis"]["bootstrap_ci_95"] = list(
        results["analysis"]["bootstrap_ci_95"]
    )

    RESULTS_DIR.mkdir(exist_ok=True)
    output_path = RESULTS_DIR / "analysis_results.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("Analysis completed successfully.")
    print(f"Total records: {total_records}")
    print(f"Valid records: {len(clean_data)}")
    print(f"Excluded records: {excluded_records}")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
