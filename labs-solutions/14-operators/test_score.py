from score import Score

s1 = Score(5)
s2 = Score(6)


def test_score_equals():
    s3 = Score(5)
    assert s1 == s3


def test_score_not_equals():
    assert s1 != s2


def test_score_add():
    assert s1 + s2 == Score(11), "Adding two scores (5 and 6) should equal 11"


def test_score_sub():
    assert s2 - s1 == Score(1), "Subtracting two scores (5 and 6) should equal 1"


def test_score_lt():
    assert s1 < s2, "S1 should be less than S2"
