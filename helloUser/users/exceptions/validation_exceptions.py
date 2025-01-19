class ValidationError(Exception):
    """Raised when input validation fails."""
    def __init__(self, message="Validation failed"):
        self.message = message
        super().__init__(self.message)
