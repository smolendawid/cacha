"""This is an example test."""

import pytest
import cache_manager as cm
import cache_manager.tests.utils as ut


def test_basic_usage():
    """Test basic caching.

    The mean is subtracked from all the columns
    so the mean after substraction should be around 0.
    """
    data = ut.download_wine_quality_data()
    data_raw = ut.remove_mean(data)
    data_cm = cm.cache(ut.remove_mean, (data,))

    assert pytest.approx(data_raw.mean()) == 0
    assert pytest.approx(data_cm.mean()) == 0
