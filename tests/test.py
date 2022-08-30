from mypackage import mypackage
from mypackage.mypackage import myModule

def test_top_n():
    """Test that the function top_n works
    """
    assert myModule.top_n([8,5,3,1,7], 3) == [8,7,5], 'Incorrect'
    assert myModule.top_n([10,11,1,5], 2) == [11, 10], 'Incorrect'
    assert myModule.top_n([1,2,3,4,5], 5) == [5,4,3,2,1], 'Incorrect'
    assert myModule.top_n([8, 3, 2, 7, 4], 3) == [8, 7, 4], 'incorrect'
    assert myModule.top_n([10, 1, 12, 9, 2], 2) == [12, 10], 'incorrect'
    assert myModule.top_n([1, 2, 3, 4, 5], 5) == [5, 4, 3, 2, 1], 'incorrect'