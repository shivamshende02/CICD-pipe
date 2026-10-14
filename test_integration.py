
from calculator import add, subtract


def test_calculation_workflow():
    total = add(10, 5)
    final_result = subtract(total, 3)

    assert total == 15
    assert final_result == 12
