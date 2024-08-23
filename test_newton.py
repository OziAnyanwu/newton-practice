import pytest
import numpy as np
import math

import newton

def test_simple():
    def f(x):
        return x**2 - 5
    
    assert np.isclose(newton.optimize(f, 7)['f(x)'], -5)
    assert np.isclose(newton.optimize(f, 7)['x'], 0, atol=1e-6)


def test_invalid_inputs():
    with pytest.raises(TypeError):
        newton.optimize(lambda x : x**2,'hello')

    with pytest.raises(TypeError):
        newton.optimize('hello', 3.5)
