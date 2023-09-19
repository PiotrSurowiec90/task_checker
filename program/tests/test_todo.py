import pytest

from lib.todo import is_task


def test_with_invalid_input():
    with pytest.raises(Exception) as e:
        result = is_task(132341234)

    error_msg = str(e.value)
    assert error_msg == "Input is invalid!"

def test_with_empty_text():
    assert is_task('') == False

def test_without_todo_in_text():
    assert is_task('This is invalid task.') == False

def test_with_uppercase_todo_in_text():
    assert is_task('#TODO This is valid task.') == True

def test_with_lowercase_todo_in_text():
    assert is_task('#todo This is valid task.') == True

def test_with_mixcase_todo_in_text():
    assert is_task('#ToDo This is valid task.') == True

def test_with_splitted_todo_in_text():
    assert is_task('#TO This is invalid task. #DO') == False

def test_with_todo_without_hashtag():
    assert is_task('This is invalid task todo.') == False