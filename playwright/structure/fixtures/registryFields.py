from typing import TypedDict, Literal

class RegistryFields(TypedDict):
    gender: Literal["Male", "Female"]
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str