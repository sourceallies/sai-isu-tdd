
def get_grades(request):
    """
    Should return the grades for a professor or grade for student

    Parameters:
    request (object):
        - type: If this is a "student" or "professor"

    **Hint**: To access an attribute in an object in Python, use `request['type']` (or similar).
    You can also look this up or ask ChatGPT :)

    Returns:
    number or list
    """
    if request['type'] == 'professor' or request['type'] == 'admin':
        return [85, 92, 95, 72]
    
    if request['type'] == 'student':
        return 92
