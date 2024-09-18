# This is for Challenge 3!

import student_grade

def test_single_homework_with_100_percent_weight_should_have_matching_grade():
    # Given:
    student_grade_example = [
        {
            "name": "Homework 1",
            "weight": 1.0,
            "grade": 90
        }
    ]

    # When:
    grade_response = student_grade.calculate(student_grade_example)

    # Then:
    assert grade_response == 90

def test_two_homeworks_with_50_percent_weight_should_average_grades():
    # Given:
    student_grade_example = [
        {
            "name": "Homework 1",
            "weight": 0.5,
            "grade": 100
        },
        {
            "name": "Homework 2",
            "weight": 0.5,
            "grade": 0
        }
    ]

    # When:
    grade_response = student_grade.calculate(student_grade_example)

    # Then:
    assert grade_response == 50

def test_four_assignments_with_a_mix_of_weights_should_have_correct_output():
    # Given:
    student_grade_example = [
        {
            "name": "Homework 1",
            "weight": 0.2,
            "grade": 95
        },
        {
            "name": "Quiz 1",
            "weight": 0.2,
            "grade": 80
        },
        {
            "name": "Homework 2",
            "weight": 0.2,
            "grade": 85
        },
        {
            "name": "Test 1",
            "weight": 0.4,
            "grade": 72
        }
    ]

    # When:
    grade_response = student_grade.calculate(student_grade_example)

    # Then:
    assert grade_response == 80.8
