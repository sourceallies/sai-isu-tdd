from numbers import Number

import grades

def test_get_grades_returns_single_number_for_student():
    request = {
        "type": "student"
    }

    assert isinstance(grades.get_grades(request), Number)

def test_get_grades_returns_number_list_for_professor():
    request = {
        "type": "professor"
    }

    assert isinstance(grades.get_grades(request), list)
