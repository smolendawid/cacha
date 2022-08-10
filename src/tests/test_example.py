"""This is an example test."""

import pytest
import cacha
import tests.utils as ut


def test_basic_usage():
    """Test basic caching.

    The mean is subtracted from all the columns
    so the mean after subtraction should be around 0.
    """
    data = ut.download_wine_quality_data()
    data_raw = ut.remove_mean(data)
    data_cm = cacha.cache(ut.remove_mean, (data,))

    assert pytest.approx(data_raw.mean()) == 0
    assert pytest.approx(data_cm.mean()) == 0


def test_basic_usage_with_kwargs():
    """Test basic caching with kwargs.

    The mean is subtracted from all the columns
    so the mean after subtraction should be around 0.
    """
    data = ut.download_wine_quality_data()
    column = "quality"
    data_cm = cacha.cache(ut.remove_mean, {"data": data, "column": column})

    assert pytest.approx(data_cm[column].mean()) == 0
