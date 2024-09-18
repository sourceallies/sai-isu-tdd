# Welcome, ISU Students!
Here we will be giving you a basic TDD interactive demo around a academic resource (like Canvas).

## Setup
1. Open this repository (success!)
2. In the top right, click `Use this template`, `Open in a codespace`
3. There will be a prompt to install Python for the codespace. Click `Install`
4. Run `pytest` in the console when the page opens. Confirm that the two existing tests **fail**

## Challenge 1 - Make green tests
When you run `pytest` in the console, you should find that the tests fail (as per step 4 above). Your challenge is to fix this tests to pass using the code in [`grades.py`](./grades.py).
We are aiming to use [red-green-refactor](https://www.codecademy.com/article/tdd-red-green-refactor) here, so aim to do the minimal possible to make these tests pass based on what you see.

## Challenge 2 - Add admin, get red tests, make green tests
You are asked to add an additional role that must be handled. An **Admin** is someoneone who has the same (or higher) level of permissions for courses as a professor. As the engineer, you must do the following:
- Write a test (first!) that checks that the result for an admin is _the same_ as a professor's. This should take the existing test for the type `professor`
- Run `pytest` to confirm that this new test **fails**
- Change `get_grades` in [`grades.py`](./grades.py) to also check for the type admin. Remember, admin should have the same result as professor, so adjust the logic you just wrote accordingly.

## Challenge 3 - Get a weighted average for a student
While [Challenge 1](#challenge-1---make-green-tests) and [Challenge 2](#challenge-2---add-admin-get-red-tests-make-green-tests) are good TDD practices, challenge 3 is going to be a bit more of a full on problem you have to solve. As you know, generally a student doesn't have just a single grade that is maintained, the system should have a grade for several homeworks, assignments, or tests with different weights. Say we have the following:

```python
student_grade = [
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
```

What would be the expected grade for this individual? Approximately 81%. If this is the outcome we want, we can start breaking this into tests. These would be some basic, practical tests, but as the engineer, you would be expected to write up more yourself:

### Given:
A single homework with 100% weight
```python
student_grade = [
    {
        "name": "Homework 1",
        "weight": 1.0,
        "grade": 90
    }
]
```

### Then:
```python
expected_grade == 90
```

### Given:
Two homeworks with 50% weight each
```python
student_grade = [
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
```

### Then:
```python
expected_grade == 50
```

You may extrapolate from here fairly well. Make a test case that is unique; given (your input) is `x`, what should the result, `y`, be?
