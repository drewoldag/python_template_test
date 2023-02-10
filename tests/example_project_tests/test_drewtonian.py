from example_project import drewtonian


def test_primary():
    """Verify the output of the `primary` function"""
    output = drewtonian.primary(5, 3)
    assert output == 15

def test_secondary():
    """Verify the output of the `secondary` function"""
    output = drewtonian.secondary()
    assert output == 10
