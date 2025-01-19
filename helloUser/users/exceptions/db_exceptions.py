class DatabaseError(Exception):
    """Raised for general database-related errors."""
    def __init__(self, message="An error occurred with the database"):
        self.message = message
        super().__init__(self.message)
