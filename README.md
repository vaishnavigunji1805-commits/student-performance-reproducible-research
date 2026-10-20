# Student Performance Reproducible Research Project

## Objective
Study the association between weekly study-time category and final Mathematics grades among students in the UCI Student Performance Mathematics dataset.

## Research Question
Is weekly study-time category associated with final Mathematics grades (G3)?

## Dataset
- Source: UCI Machine Learning Repository
- File: student-mat.csv
- Population: Students represented by Mathematics records from two Portuguese secondary schools.
- Unit of analysis: One student record.
- Study design: Observational, cross-sectional analysis.
- Observation window: Existing student records; no longitudinal follow-up period.

## Variables
- Exposure: studytime, an ordinal category of weekly study time.
- Outcome: G3, final Mathematics grade on a 0–20 scale.

## Hypotheses
- H0: There is no monotonic association between studytime and G3.
- H1: There is a monotonic association between studytime and G3.

## Analysis Plan
- Two-sided Spearman rank correlation.
- Significance level: 0.05.
- Effect size: Spearman's rho.
- Uncertainty: 95% bootstrap confidence interval using 5,000 resamples and a fixed random seed.
- Robustness check: Kendall's tau-b.
- Report sample size, exclusions, missingness, effect size, confidence interval, p-value, and interpretation.
- Correlation does not establish causation.

## Project Structure
- data/: Dataset files.
- notebooks/: Research notebooks.
- src/: Analysis code.
- tests/: Automated tests.
- preregistration.md: Registered research question and analysis plan.
- requirements.txt: Python dependencies.

## Reproducibility
Activate the project's virtual environment before running commands.

Install dependencies:

    python -m pip install -r requirements.txt

Run automated tests:

    python -m pytest -v

## Research Integrity
Do not inspect real outcome patterns until the preregistration has been committed. Preserve raw data, document analysis deviations, and record any deviations from the registered plan.