
import Swapping_two_number


def test_swap_pass():
    """Test case that should pass."""
    a, b = 5, 9
    swapped_a, swapped_b = Swapping_two_number.swap(a, b)
    assert swapped_a == 9
    assert swapped_b == 5

def test_swap_fail():
    """Test case that should fail."""
    a, b = 5, 9
    swapped_a, swapped_b = Swapping_two_number.swap(a, b)
    assert swapped_a == 5  # This is incorrect; the correct result should be 9
    assert swapped_b == 9  # This is incorrect; the correct result should be 5
