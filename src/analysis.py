
import numpy as np
from scipy.stats import spearmanr, kendalltau


def analyze_student_data(data, bootstrap_samples=5000, seed=42):
    """Analyze study-time category and final Mathematics grade."""

    required_columns = {"studytime", "G3"}

    if not required_columns.issubset(data.columns):
        raise ValueError("Data must contain studytime and G3 columns.")

    clean_data = data[["studytime", "G3"]].dropna().copy()

    if clean_data.empty:
        raise ValueError("No valid records available.")

    if not clean_data["studytime"].between(1, 4).all():
        raise ValueError("studytime values must be between 1 and 4.")

    if not clean_data["G3"].between(0, 20).all():
        raise ValueError("G3 values must be between 0 and 20.")

    if len(clean_data) < 3:
        raise ValueError("At least 3 valid records are required.")

    if clean_data["studytime"].nunique() < 2:
        raise ValueError("studytime must contain at least 2 distinct values.")

    if clean_data["G3"].nunique() < 2:
        raise ValueError("G3 must contain at least 2 distinct values.")

    if bootstrap_samples < 1:
        raise ValueError("bootstrap_samples must be positive.")

    studytime = clean_data["studytime"].to_numpy()
    grades = clean_data["G3"].to_numpy()

    spearman = spearmanr(studytime, grades)
    kendall = kendalltau(studytime, grades)

    # Bootstrap confidence interval for Spearman's rho.
    rng = np.random.default_rng(seed)
    n = len(clean_data)
    bootstrap_rhos = []

    for _ in range(bootstrap_samples):
        indices = rng.integers(0, n, size=n)
        sampled_studytime = studytime[indices]
        sampled_grades = grades[indices]

        # Skip samples with no variation in either variable.
        if (
            np.unique(sampled_studytime).size < 2
            or np.unique(sampled_grades).size < 2
        ):
            continue

        rho = spearmanr(sampled_studytime, sampled_grades).statistic
        if np.isfinite(rho):
            bootstrap_rhos.append(rho)

    if len(bootstrap_rhos) < 100:
        raise ValueError(
            "Too few valid bootstrap samples to estimate a confidence interval."
        )

    ci_lower, ci_upper = np.percentile(
        bootstrap_rhos, [2.5, 97.5]
    )

    return {
        "n": n,
        "spearman_rho": float(spearman.statistic),
        "p_value": float(spearman.pvalue),
        "bootstrap_ci_95": (float(ci_lower), float(ci_upper)),
        "valid_bootstrap_samples": len(bootstrap_rhos),
        "kendall_tau_b": float(kendall.statistic),
        "kendall_p_value": float(kendall.pvalue),
    }
