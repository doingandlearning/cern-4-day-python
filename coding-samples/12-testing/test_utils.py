import mock
import builtins

from utils import get_user_yes_or_no


def test_get_user_yes_or_no_with_y():
    with mock.patch.object(builtins, 'input', lambda _: 'y'):
        response = get_user_yes_or_no('input name: ')
        assert response == 'y'


def test_get_user_yes_or_no_with_n():
    with mock.patch.object(builtins, 'input', lambda _: 'n'):
        response = get_user_yes_or_no('input name: ')
        assert response == 'n'


def test_get_user_yes_or_no_with_Y():
    with mock.patch.object(builtins, 'input', lambda _: 'Y'):
        response = get_user_yes_or_no('input name: ')
        assert response == 'y'


def test_get_user_yes_or_no_with_N():
    with mock.patch.object(builtins, 'input', lambda _: 'N'):
        response = get_user_yes_or_no('input name: ')
        assert response == 'n'


def test_get_user_yes_or_no_with_H():
    count = 0

    def generate_input(prompt):
        nonlocal count
        if count == 0:
            count = count + 1
            return 'H'
        else:
            return 'y'

    with mock.patch.object(builtins, 'input', generate_input):
        response = get_user_yes_or_no('input name: ')
        assert response == 'y'
