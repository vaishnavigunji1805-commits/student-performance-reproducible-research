# Student Performance Reproducible Research Project

## 1. Objective

Study the association between weekly study-time category and final Mathematics grades among students represented in the UCI Student Performance dataset.

## 2. Research Question

Is weekly study-time category associated with final Mathematics grades (G3)?

## 3. Dataset

- **Source:** [UCI Machine Learning Repository — Student Performance](https://archive.ics.uci.edu/dataset/320/student+performance)
- **File:** `data/student-mat.csv`
- **Records analyzed:** 395
- **Population:** Students represented by Mathematics records collected from two Portuguese secondary schools.
- **Unit of analysis:** One student record.
- **Study design:** Observational analysis using existing student records.

## 4. Variables

- **Exposure:** `studytime`, an ordinal category representing weekly study time.
- **Outcome:** `G3`, the final Mathematics grade on a 0–20 scale.

Study-time categories range from 1 (less than 2 hours per week) to 4 (more than 10 hours per week). These categories are ordinal and are not converted into exact hours.

## 5. Hypotheses

- **Null hypothesis (H0):** There is no monotonic association between `studytime` and `G3`.
- **Alternative hypothesis (H1):** There is a monotonic association between `studytime` and `G3`.

## 6. Preregistered Analysis Plan

- Primary test: Two-sided Spearman rank correlation.
- Significance level: 0.05.
- Effect size: Spearman's rho.
- Uncertainty: 95% bootstrap confidence interval using 5,000 resamples and a fixed random seed.
- Robustness check: Kendall's tau-b.
- Report sample size, exclusions, effect sizes, confidence intervals, p-values, and interpretation.
- Do not interpret correlation as proof of causation.

The preregistration is recorded in `preregistration.md`.

## 7. Results

The analysis included 395 records. No records were excluded under the implemented missing-value and validity rules.

| Measure | Result |
|---|---:|
| Total records | 395 |
| Valid records analyzed | 395 |
| Excluded records | 0 |
| Spearman's rho | 0.1052 |
| Spearman p-value | 0.0367 |
| 95% bootstrap confidence interval | 0.0011 to 0.2064 |
| Valid bootstrap resamples | 5,000 |
| Kendall's tau-b | 0.0851 |
| Kendall p-value | 0.0338 |

### Interpretation

The results indicate a weak positive association between weekly study-time category and final Mathematics grades. The Spearman p-value is below the preregistered 0.05 significance threshold, and the Kendall robustness check points in the same direction.

The lower bound of the bootstrap confidence interval is close to zero, so the estimated association is small and uncertain in magnitude. Because this is observational research, the findings do not establish that increased study time causes higher grades.

## 8. Project Structure

- `data/`: Dataset file.
- `notebooks/`: Research notebooks.
- `src/analysis.py`: Statistical analysis function.
- `src/run_analysis.py`: Loads the dataset, runs the analysis, and saves the results.
- `tests/`: Automated tests using synthetic data.
- `results/analysis_results.json`: Saved statistical results.
- `preregistration.md`: Registered research question and analysis plan.
- `requirements.txt`: Main Python dependencies.
- `requirements-lock.txt`: Recorded package versions for reproducibility.
- `README.md`: Project overview, methods, and findings.

## 9. Reproducing the Analysis

Run the commands below from the project root in PowerShell.

Install the recorded package versions:

    python -m pip install -r requirements-lock.txt

Run automated tests:

    python -m pytest -v

Run the real-data analysis:

    python src/run_analysis.py

Read the saved results:

    Get-Content results/analysis_results.json

The analysis uses a fixed bootstrap random seed. Results may still vary across software environments or package versions.

## 10. Research Integrity

- Commit the preregistration before inspecting real outcome patterns.
- Preserve the original dataset.
- Apply the predefined inclusion, exclusion, and validity rules.
- Record deviations from the registered plan, including the reason and potential impact.
- Distinguish statistical association from causal effects.

## 11. Version Control

The project uses Git to track the preregistration, analysis code, tests, environment information, and saved results. Check `git status` to verify whether there are uncommitted changes.
