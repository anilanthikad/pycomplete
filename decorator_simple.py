import functools

user = {'username': 'supandi',
        'access_level': 'admin'
        }


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


@user_has_permission
def my_function():
    """
    Allows us to retrieve the password for the admin panel.
    """
    return 'Password for admin panel is 1234'


@user_has_permission
def another():
    pass

print(my_function.__name__)
print(another.__name__)
