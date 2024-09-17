from numbers import Number

import grades

def test_get_grades_returns_single_number_for_student():
    request = {
        "type": "student"
    }

    assert isinstance(grades.get_grades(request), Number)

def test_get_grades_returns_number_list_for_teacher():
    request = {
        "type": "teacher"
    }

    assert isinstance(grades.get_grades(request), list)
