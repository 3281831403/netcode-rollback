import pytest

from net import rollback as mod

CASES = [
    ('dedupe_inputs', [[1, 2, 3, 5], 2], [3, 5], False),
    ('reconcile', [0.0, 10.0, 0.25], 2.5, True),
    ('tick_drift', [100, 98], 2, False),
    ('interp_delay', [1.0, 2.0], 0.0, True),
    ('interp_delay', [2.0, 1.0], 1.0, True),
    ('rollback_depth', [10, 4, 3], 3, False),
    ('state_hash', [[1, 2, 3]], 'a01eda32e4e0b139', False),
    ('resend_missing', [[1, 2, 3], [1, 3]], [2], False),
    ('is_desync', ['a', 'a'], False, False),
    ('is_desync', ['a', 'b'], True, False),
    ('ring_index', [12, 5], 2, False),
    ('commit_batch', [[True, True]], True, False),
    ('dedupe_inputs', [[], 0], [], False),
    ('reconcile', [5.0, 5.0, 0.5], 5.0, True),
    ('rollback_depth', [2, 10, 3], 0, False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_rollback_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
