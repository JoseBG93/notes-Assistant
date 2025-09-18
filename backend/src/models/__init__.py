"""
Models package for Notes Assistant.

Contains data models for the application:
- User: User model with validation
- Note: Note model with CRUD operations
"""

from .user import User
from .note import Note

__all__ = ['User', 'Note'] 