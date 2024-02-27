def greet_user(username):
    
    """greet message for guest"""#document string, to explain function
    print(f"Hello, {username}")


greet_user('kim')
help(greet_user)
print(greet_user.__doc__)