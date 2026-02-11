# Creating Decorator
def admin_only(func):
    def wrapper(username):
        if username == "admin":
            return func(username)
        else:
            print("Access Denied")
    return wrapper


# Applying Decorator
@admin_only
def dashboard(username):
    print(f"Welcome {username}! You have access to the dashboard.")


# Testing

# Case 1: Admin user (Allowed)
dashboard("admin")

# Case 2: Other user (Blocked)
dashboard("rahul")
