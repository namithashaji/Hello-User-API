from dataclasses import dataclass
from typing import Optional

@dataclass
class UpdateUserRequest:
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
