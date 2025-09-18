"""
Services package for Notes Assistant.

Contains business logic services:
- DataService: Handles data persistence with JSON files
- UserService: Manages user operations
- NotesService: Manages notes operations
"""

from .data_service import DataService
from .user_service import UserService
from .notes_service import NotesService

__all__ = ['DataService', 'UserService', 'NotesService'] 