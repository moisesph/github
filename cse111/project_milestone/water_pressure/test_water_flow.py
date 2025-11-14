from pytest import approx
import pytest
from waterflow import water_column_height, \
pressure_gain_from_water_height, \
pressure_loss_from_pipe, \
pressure_loss_from_fittings, \
reynolds_number, \
pressure_loss_from_pipe_reduction

 


def test_water_column_height(): #passed
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=0.001)

def test_pressure_gain_from_water_height(): #Passed
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe(): #Passed
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def  test_pressure_loss_from_fittings(): #Passed
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def  test_reynolds_number(): #Passed 
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)

def  test_pressure_loss_from_pipe_reduction(): #Passed
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])