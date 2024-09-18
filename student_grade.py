# This is for Challenge 3!

def calculate(student_grade):
    """
    Should return the combined weighted average of all assignments in student_grade

    Parameters:
    student_grade (object[]):
        - name (str): The given assignment name
        - weight (float): The weight of this assignment
            (between 0 and 1, all assignments in student_grade should add up to 1)
        - grade (float): The grade received on this assignment

    Returns:
    number
    """
    sum = 0
    for assignment in student_grade:
        sum += assignment['grade'] * assignment['weight']

    return sum
