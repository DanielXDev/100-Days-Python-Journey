class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper

@is_authenticated
def create_new_post(user):
    print(f"This is {user.name} new post!!!")


new_user = User("Daniel")
new_user.is_logged_in = True
create_new_post(new_user)