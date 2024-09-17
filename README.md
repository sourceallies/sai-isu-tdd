# Welcome, ISU Students!
Here we will be giving you a basic TDD interactive demo.

## Setup
1. Open this repository (success!)
2. In the top right, click `Use this template`, `Open in a codespace`
3. There will be a prompt to install Python for the codespace. Click `Install`
4. Run `pytest` in the console when the page opens. Confirm that the two existing tests **fail**

## Challenge 1 - Get green tests
When you run `pytest` in the console, you should find that the tests fail (as per step 4 above). Your challenge is to fix this tests to pass using the code in [`grades.py`](./grades.py).
We are aiming to use [red-green-refactor](https://www.codecademy.com/article/tdd-red-green-refactor) here, so aim to do the minimal possible to make these tests pass based on what you see.

## Challenge 2 - Add admin, get red tests, get green tests
You are asked to add an additional role that must be handled. An **Admin** is someoneone who has the same (or higher) level of permissions for courses as a professor. As the engineer, you must do the following:
- Write a test (first!) that checks that the result for an admin is _the same_ as a professor's. This should take the existing test for the type `professor`
- Run `pytest` to confirm that this new test **fails**
- Change `get_grades` in [`grades.py`](./grades.py) to also check for the type admin. Remember, admin should have the same result as professor, so adjust the logic you just wrote accordingly.
