import pytest

import simulate_turbidity_dosing as sim


def test_compute_total_stock():
    assert sim.compute_total_stock(10, 110, 1000) == pytest.approx(100)


def test_compute_total_volume():
    assert sim.compute_total_volume(1000, 100) == 1100


def test_is_valid_target():
    assert sim.is_valid_target(10, 100)
    assert not sim.is_valid_target(0, 100)
    assert not sim.is_valid_target(100, 100)


def test_validate_inputs_rejects_non_positive():
    with pytest.raises(ValueError):
        sim.validate_inputs(0, 1000)
    with pytest.raises(ValueError):
        sim.validate_inputs(4000, 0)
