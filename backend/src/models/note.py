from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Note:
    """Note model for the notes application."""
    id: int
    title: str
    content: str
    created_at: str
    updated_at: Optional[str] = None
    user_id: Optional[int] = None
    
    def __post_init__(self):
        """Validate note data after initialization."""
        self.validate_title()
        self.validate_content()
    
    def validate_title(self):
        """Validate that title is not empty and not too long."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        if len(self.title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
    
    def validate_content(self):
        """Validate that content is not empty."""
        if not self.content or not self.content.strip():
            raise ValueError("Content cannot be empty")
    
    def update_content(self, new_content: str):
        """Update note content and timestamp."""
        if not new_content or not new_content.strip():
            raise ValueError("Content cannot be empty")
        self.content = new_content
        self.updated_at = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    
    def update_title(self, new_title: str):
        """Update note title and timestamp."""
        if not new_title or not new_title.strip():
            raise ValueError("Title cannot be empty")
        if len(new_title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        self.title = new_title
        self.updated_at = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    
    def to_dict(self) -> dict:
        """Convert note object to dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'user_id': self.user_id
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Note':
        """Create note object from dictionary."""
        return cls(**data)
    
    def get_summary(self, max_length: int = 50) -> str:
        """Get a summary of the note content."""
        if len(self.content) <= max_length:
            return self.content
        return self.content[:max_length] + "..."
    
    def __str__(self) -> str:
        """String representation of the note."""
        return f"Note {self.id}: {self.title}" 