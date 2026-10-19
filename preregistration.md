# Analysis Preregistration: Student Performance

## 1. Research Question

Is weekly study-time category associated with final Mathematics grades among students represented in the UCI Student Performance Mathematics dataset?

## 2. Dataset and Population

- Dataset source: UCI Machine Learning Repository
- Dataset file: student-mat.csv
- Population: Students represented by the Mathematics records collected from two Portuguese secondary schools.
- Unit of analysis: One student record.
- Study design: Observational analysis.

## 3. Hypotheses

- H0: There is no monotonic association between weekly study-time category and final Mathematics grade.
- H1: There is a monotonic association between weekly study-time category and final Mathematics grade.
- Statistical test: Two-sided.
- Significance level: 0.05.

## 4. Variables

- Exposure: studytime, an ordinal category representing weekly study time.
- Outcome: G3, final Mathematics grade on a 0–20 scale.

Study-time categories:
1 = Less than 2 hours
2 = 2–5 hours
3 = 5–10 hours
4 = More than 10 hours

Do not convert categories into exact hours.

## 5. Inclusion and Exclusion

Include records with valid values for both studytime and G3.

Exclude records only when either primary variable is missing or invalid. Report exclusions and their reasons. Do not exclude records based on whether they support the hypothesis.

## 6. Analysis Plan

- Primary test: Spearman rank correlation.
- Effect size: Spearman's rho.
- Uncertainty: 95% bootstrap confidence interval using 5,000 resamples and a fixed random seed.
- Report sample size, effect size, confidence interval, p-value, and interpretation.
- Robustness check: Kendall's tau-b.
- Missing data: Report missingness and exclude records with missing primary variables according to the predefined rules.
- Do not interpret association as proof of causation.

## 7. Deviations

Record the date, original decision, change, reason, and potential impact of every deviation from this plan.

## 8. Status

Draft pending Git commit. Do not begin analysis of the real dataset until the preregistration has been committed.
