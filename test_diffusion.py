"""tests from the diffusion model module"""

from DiffusionModel import calculate_stable_time_step

def test_time_step_is_float():
    time_step = calculate_stable_time_step(1,1)
    assert isinstance(time_step, float)
    