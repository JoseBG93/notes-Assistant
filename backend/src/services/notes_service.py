from typing import List, Optional
from datetime import datetime

from models.note import Note
from models.user import User
from services.data_service import DataService


class NotesService:
     # Note-specific operations and user-note association
    """Service for handling notes business logic."""
    
    def __init__(self, data_service: DataService):
        self.data_service = data_service
    
    # Note creation method - creates a new note
    def create_note(self, title: str, content: str, user_id: int) -> Note:
        """Create a new note."""
        note_id = self.data_service.get_next_note_id()
        created_at = datetime.now().strftime('%d/%m/%y %H:%M:%S')
        
        note = Note(
            id=note_id,
            title=title.strip(),
            content=content.strip(),
            created_at=created_at,
            user_id=user_id
        )
        
        return self.data_service.save_note(note)
    
    # Single note retrieval method - returns a single note (with ownership check)
    def get_note(self, note_id: int, user_id: int) -> Optional[Note]:
        """Get a note by ID, ensuring it belongs to the user."""
        note = self.data_service.get_note_by_id(note_id)
        if note and note.user_id == user_id:
            return note
        return None
    
    # User notes retrieval method - returns all notes for a user
    def get_user_notes(self, user_id: int) -> List[Note]:
        """Get all notes for a user."""
        return self.data_service.get_notes_by_user(user_id)
    
    # Note title update method - updates a note's title
    def update_note_title(self, note_id: int, new_title: str, user_id: int) -> Optional[Note]:
        """Update a note's title."""
        note = self.get_note(note_id, user_id)
        if note:
            note.update_title(new_title.strip())
            return self.data_service.save_note(note)
        return None
    
    # Note content update method - updates a note's content
    def update_note_content(self, note_id: int, new_content: str, user_id: int) -> Optional[Note]:
        """Update a note's content."""
        note = self.get_note(note_id, user_id)
        if note:
            note.update_content(new_content.strip())
            return self.data_service.save_note(note)
        return None
    
    # Note deletion method - deletes a note (with ownership check)
    def delete_note(self, note_id: int, user_id: int) -> bool:
        """Delete a note, ensuring it belongs to the user."""
        note = self.get_note(note_id, user_id)
        if note:
            return self.data_service.delete_note(note_id)
        return False
    
    # Note search method - searches notes by title or content
    def search_notes(self, query: str, user_id: int) -> List[Note]:
        """Search notes by title or content."""
        user_notes = self.get_user_notes(user_id)
        query_lower = query.lower()
        
        matching_notes = []
        for note in user_notes:
            if (query_lower in note.title.lower() or 
                query_lower in note.content.lower()):
                matching_notes.append(note)
        
        return matching_notes
    
    # Note summary method - returns a summary of user's notes.
    def get_notes_summary(self, user_id: int) -> dict:
        """Get a summary of user's notes."""
        notes = self.get_user_notes(user_id)
        
        return {
            'total_notes': len(notes),
            'recent_notes': notes[:5],  # First 5 (most recent)
            'oldest_note': notes[-1] if notes else None,
            'newest_note': notes[0] if notes else None
        } 