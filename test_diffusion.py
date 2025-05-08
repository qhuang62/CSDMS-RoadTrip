"""tests from the diffusion model module"""

import pytest
from DiffusionModel import calculate_stable_time_step

def test_time_step_is_float():
    time_step = calculate_stable_time_step(1,1)
    assert isinstance(time_step, float)

def test_time_step_with_zero_spacing():
    dt = calculate_stable_time_step(dx=0.0, diffusivity=1)
    assert dt == pytest.approx(0.0)
    assert math.isclose(dt, 0.0)
    