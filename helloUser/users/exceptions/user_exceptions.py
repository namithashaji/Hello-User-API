class UserNotFoundError(Exception):
    """Raised when the requested user does not exist."""
    def __init__(self, message="User not found"):
        self.message = message
        super().__init__(self.message)


class DuplicateUserError(Exception):
    """Raised when trying to create a user with duplicate data."""
    def __init__(self, message="A user with this email already exists"):
        self.message = message
        super().__init__(self.message)
