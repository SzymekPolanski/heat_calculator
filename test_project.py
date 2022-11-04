from class_project import Heat_calculator
import pytest

def test_calculate_resistance():
    calculator = Heat_calculator(["cegła pełna", "wełna mineralna", -15, 25, 0.5, 5])
    assert calculator.calculate_resistance() == 12.030844155844155
    calculator = Heat_calculator(["cegła dziurawka", "styropian", 5, 21, 0.7, 3])
    assert calculator.calculate_resistance() == 16.764976958525345
    calculator = Heat_calculator(["pustak ceramiczny", "styropian", 5, 30, 1, 10])
    assert calculator.calculate_resistance() == 22.23502304147465
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", -40, 35, 0.2, 13])
    assert calculator.calculate_resistance() == 2.714285714285715
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", 0, 0, 2, 2])
    assert calculator.calculate_resistance() == 58.96428571428571
    calculator = Heat_calculator(["pustak ceramiczny", "wełna mineralna", -23.7, 24.8, 0.246, 23.8])
    assert calculator.calculate_resistance() == 0.6814516129032258


def test_heat_transfer_coefficient_k():
    calculator = Heat_calculator(["cegła pełna", "wełna mineralna", -15, 25, 5, 10])
    assert calculator.heat_transfer_coefficient_k() == 0.006543395663846171
    calculator = Heat_calculator(["cegła dziurawka", "styropian", 5, 21, 0.7, 3])
    assert calculator.heat_transfer_coefficient_k() == 0.05904936838001339
    calculator = Heat_calculator(["pustak ceramiczny", "styropian", 5, 30, 1, 10])
    assert calculator.heat_transfer_coefficient_k() == 0.04463283818315322
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", -40, 35, 0.2, 13])
    assert calculator.heat_transfer_coefficient_k() == 0.3467056651515088
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", 0, 0, 2, 2])
    assert calculator.heat_transfer_coefficient_k() == 0.01691066189406021
    calculator = Heat_calculator(["pustak ceramiczny", "wełna mineralna", -23.7, 24.8, 0.246, 23.8])
    assert calculator.heat_transfer_coefficient_k() == 1.174457687813886


def test_init_heat_calculator():
    calculator = Heat_calculator(["cegła pełna", "wełna mineralna", -15, 25, 0.5, 5])
    assert calculator.heat == 16.39
    calculator = Heat_calculator(["cegła dziurawka", "styropian", 5, 21, 0.7, 3])
    assert calculator.heat == 2.83
    calculator = Heat_calculator(["pustak ceramiczny", "styropian", 5, 30, 1, 10])
    assert calculator.heat == 11.16
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", -40, 35, 0.2, 13])
    assert calculator.heat == 338.04
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", 0, 0, 2, 2])
    assert calculator.heat == 0.0
    calculator = Heat_calculator(["pustak ceramiczny", "wełna mineralna", -23.7, 24.8, 0.246, 23.8])
    assert calculator.heat == 1355.68


def test_str_heat_calculator():
    calculator = Heat_calculator(["cegła pełna", "wełna mineralna", -15, 25, 0.5, 5])
    assert calculator.__str__() == "Ucieka Ci 16.39 [W] ciepła..."
    calculator = Heat_calculator(["cegła dziurawka", "styropian", 5, 21, 0.7, 3])
    assert calculator.__str__() == "Ucieka Ci 2.83 [W] ciepła..."
    calculator = Heat_calculator(["pustak ceramiczny", "styropian", 5, 30, 1, 10])
    assert calculator.__str__() == "Ucieka Ci 11.16 [W] ciepła..."
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", -40, 35, 0.2, 13])
    assert calculator.__str__() == "Ucieka Ci 338.04 [W] ciepła..."
    calculator = Heat_calculator(["cegła kratówka", "wełna mineralna", 0, 0, 2, 2])
    assert calculator.__str__() == "Ucieka Ci 0.0 [W] ciepła..."
    calculator = Heat_calculator(["pustak ceramiczny", "wełna mineralna", -23.7, 24.8, 0.246, 23.8])
    assert calculator.__str__() == "Ucieka Ci 1355.68 [W] ciepła..."



# def test_errors_calc_res():
#     with pytest.raises(KeyError):
#         calculate_resistance('hello')
#     with pytest.raises(TypeError):
#         calculate_resistance(12345)

# def test_errors_heat_coe():
#     with pytest.raises(TypeError):
#         heat_transfer_coefficient_k('hello')

# def test_errors_heat_cal():
#     with pytest.raises(IndexError):
#         heat_calculator('hello', 'see you')
#     with pytest.raises(TypeError):
#         heat_calculator((1,2,3,4,5,6), 'see you')

    

calculator = Heat_calculator(["cegła pełna", "wełna mineralna", 'hello', 'hi', 'bye', 'goodbye'])
# calculator.calculate_resistance() == 12.030844155844155
