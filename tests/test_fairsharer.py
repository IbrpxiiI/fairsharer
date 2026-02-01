from fairsharer.fairsharer import fair_sharer

def test_fair_sharer_one_iteration():
    values = [0, 1000, 800, 0]
    assert fair_sharer(values, 1) == [100, 800, 900, 0]


def test_fair_sharer_two_iterations():
    values = [0, 1000, 800, 0]
    assert fair_sharer(values, 2) == [100, 890, 720, 90]

