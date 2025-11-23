import Lab_2_revision.bmi as bmi
#pycache file is a folder tht python auto create that stores comiple byte code and make ur code run faster

def test_bmi_normal_weight():
    #arrange
    height = 1.73
    weight = 57

    #act
    x = bmi.calculate_bmi(height,weight)

    #assert
    assert x == 0

def test_bmi_over_weight():
     #arrange
    height = 1.73
    weight = 80

    #act
    x = bmi.calculate_bmi(height,weight)

    #assert
    assert x == 1

def test_bmi_under_weight():
     #arrange
    height = 1.73
    weight = 40

    #act
    x = bmi.calculate_bmi(height,weight)

    #assert
    assert x == -1
