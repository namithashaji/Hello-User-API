from dataclasses import dataclass

@dataclass
class UserDetailsResponse:
    id: int
    name: str
    email: str
    age: int
