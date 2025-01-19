from ..models import User
from ..exceptions import UserNotFoundError, DuplicateUserError, DatabaseError
from string import Template


def create_user(user_data):
    """Handles user creation."""
    try:
        # Check for duplicate user
        if User.objects.filter(email=user_data.email).exists():
            raise DuplicateUserError("A user with this email already exists.")

        # Create the user
        user = User.objects.create(
            name=user_data.name,
            email=user_data.email,
            age=user_data.age
        )
        return user

    except Exception as e:
        raise DatabaseError(f"Database error: {str(e)}")


def update_user(user_id, user_data):
    """Handles user updates."""
    try:
        user = User.objects.get(id=user_id)

        # Update fields
        if user_data.name:
            user.name = user_data.name
        if user_data.email:
            user.email = user_data.email
        if user_data.age:
            user.age = user_data.age
        user.save()
        return user

    except User.DoesNotExist:
        raise UserNotFoundError(f"User with ID {user_id} not found.")
    except Exception as e:
        raise DatabaseError(f"Database error: {str(e)}")


def delete_user(user_id):
    """Handles user deletion."""
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return user
    except User.DoesNotExist:
        raise UserNotFoundError(f"User with ID {user_id} not found.")
    except Exception as e:
        raise DatabaseError(f"Database error: {str(e)}")


def get_user_by_id(user_id):
    """Fetch a user by ID."""
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        raise UserNotFoundError(f"User with ID {user_id} not found.")
    except Exception as e:
        raise DatabaseError(f"Failed to retrieve user: {str(e)}")


def greet_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        greet_template = Template("Hello $name !")
        greet_msg = greet_template.substitute(name=user.name)
        print(greet_msg)
        return greet_msg
    except User.DoesNotExist:
        raise UserNotFoundError(f"User with ID {user_id} not found.")
    except Exception as e:
        raise DatabaseError(f"Failed to retrieve user: {str(e)}")
