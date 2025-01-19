from dataclasses import dataclass

@dataclass
class CreateUserRequest:
    name: str
    email: str
    age: int
