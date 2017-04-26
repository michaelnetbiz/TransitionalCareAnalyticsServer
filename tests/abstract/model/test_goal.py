from tcas.abstract.model.goal import Goal


def test_create_goal():
    """Test goal creation.

    """
    g = Goal('1', 'ba_goal1')
    assert type(g) is Goal
