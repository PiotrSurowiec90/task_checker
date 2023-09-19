"""As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO."""



def is_task(text):
    """
    Checks if given text contains string TODO and therefrore is a task.

    parameters:
        text - string: Text to perform task check.

    returns:
        boolean: True if given text is a task or False otherwise
    """

    if type(text) != str:
        raise Exception("Input is invalid!")

    return '#TODO' in text.upper()