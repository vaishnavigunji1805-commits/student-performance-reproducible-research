
import pandas as pd
import pytest

from src.analysis import analyze_student_data


def test_synthetic_data_returns_expected_outputs():
    # Artificial data; not taken from real students.
    data = pd.DataFrame({
        "studytime": [1, 2, 3, 4, 1, 2],
        "G3": [8, 10, 13, 17, 9, 11],
    })

    result = analyze_student_data(data)

    assert result["n"] == 6
    assert -1 <= result["spearman_rho"] <= 1
    assert 0 <= result["p_value"] <= 1


def test_missing_values_are_excluded():
    data = pd.DataFrame({
        "studytime": [1, 2, 3, 4],
        "G3": [8, None, 14, 17],
    })

    result = analyze_student_data(data)

    assert result["n"] == 3


def test_missing_columns_raise_error():
    data = pd.DataFrame({"studytime": [1, 2, 3]})

    with pytest.raises(ValueError):
        analyze_student_data(data)


def test_invalid_grades_raise_error():
    data = pd.DataFrame({
        "studytime": [1, 2, 3],
        "G3": [8, 25, 14],
    })

    with pytest.raises(ValueError):
        analyze_student_data(data)
