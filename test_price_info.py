import price_info as price

def test_total():
    result = 0
    expected = 46.75

    result = price.total_cost_shopping()

    assert result == expected

def test_cost_of_fruit():
    result = 0

    expected = 2.4

    result = price.cost_of_fruits('apple',2)

    assert result == expected