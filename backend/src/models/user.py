from dataclasses import dataclass
from typing import Optional
import re


@dataclass
class User:
    """User model for the notes application."""
    id: int
    name: str
    surname: str
    birthday: str       # DD-MM-YYYY format
    favorite_color: str
    
    def __post_init__(self):
        """Validate user data after initialization."""
        self.validate_name()
        self.validate_birthday()
        self.validate_color()
    
    # Validation methods for data integrity
    
    def validate_name(self):
        """Validate that name and surname contain only letters."""
        if not self.name.replace(' ', '').isalpha():
            raise ValueError("Name must contain only letters")
        if not self.surname.replace(' ', '').isalpha():
            raise ValueError("Surname must contain only letters")
    
    def validate_birthday(self):
        """Validate birthday format (DD-MM-YYYY or DD/MM/YYYY)."""
        pattern1 = re.compile(r'^\d{2}-\d{2}-\d{4}$')
        pattern2 = re.compile(r'^\d{2}/\d{2}/\d{4}$')
        if not (pattern1.match(self.birthday) or pattern2.match(self.birthday)):
            raise ValueError("Birthday must be in DD-MM-YYYY or DD/MM/YYYY format")
    
    def validate_color(self):
        """Validate that color is a valid CSS color name."""
        # Basic color validation - can be extended
        valid_colors = [
            'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 
            'brown', 'black', 'white', 'gray', 'grey', 'cyan', 'magenta'
        ]
        if self.favorite_color.lower() not in valid_colors:
            raise ValueError(f"Color must be one of: {', '.join(valid_colors)}")
    
    def to_dict(self) -> dict:
        """Convert user object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'birthday': self.birthday,
            'favorite_color': self.favorite_color
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'User':
        """Create user object from dictionary."""
        return cls(**data) 