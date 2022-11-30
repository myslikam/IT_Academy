from task1 import *

def test_d_glazing():
    temp = specThermalChar(190, 43, 102.37, 9)
    res = temp.d_glazing()
    assert res == 0.08791638175246654
    return print("test_d_glazing = ОК")

def test_q_char():
    temp = specThermalChar(190, 43, 102.37, 9)
    res = temp.q_char()
    assert res == 0.859842105263158
    return print("test_q_char = ОК")


def test_thermLoad():
    temp = thermLoad(190, 43, 102.37, 9, 18, -24, 188, -1)
    res = temp.Qmax()
    assert res == 0.00686154
    return print("test_thermLoad = ОК")

def test_boilerEfficiency():
    temp = boilerEfficiency(75)
    res = temp.b_boiler()
    assert res == 190.48
    return print("test_boilerEfficiency = ОК")

def test_calculation_fuel():

    Qmax_calc = thermLoad(190, 43, 102.37, 9, 18, -24, 188, -1)
    b_calc = boilerEfficiency(75)

    res = Qmax_calc.Qmax() * ((Qmax_calc.tvn - Qmax_calc.tsrn) / (Qmax_calc.tvn - Qmax_calc.trnv)) \
          * Qmax_calc.N *24 * b_calc.b_boiler() / 1000

    assert res == 2.6677454224128003
    return print("test_calculation_fuel = ОК")




test_d_glazing()
test_q_char()
test_thermLoad()
test_boilerEfficiency()
test_calculation_fuel()