from mergeIntervals import mergeIntervals
def test_case_one():
    assert mergeIntervals([[1,3],[2,6], [8, 10], [15,18]]) == [[1,6], [8, 10], [15,18]]
def test_unsorted_case():
    assert mergeIntervals([[8, 10], [2,6], [15,18], [1,3]]) == [[1,6], [8, 10], [15,18]]
def test_case_length_one():
    assert mergeIntervals([[1,3]]) == [[1,3]]
def test_case_two():
    assert mergeIntervals([[1,4],[4,5]]) == [[1,5]]