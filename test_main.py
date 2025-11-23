import Lab_2_revision.main as main

def test_min_max():
    input_arr = [1,2,3]
    test_arr = [1,3]
    result = []

    result = main.find_min_max(input_arr)

    assert result == test_arr

def test_average():
    result = []
    input_arr = [1,2,3]
    expected = 2.0

    result = main.calc_avergae(input_arr)

    assert result == expected

def test_median():
    result = []
    input_arr = [1,2,4]
    excepted = 2

    result = main.calc_median_temperature(input_arr)

    assert result == excepted