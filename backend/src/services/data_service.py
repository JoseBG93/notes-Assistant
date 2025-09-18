import json
import os
from typing import Dict, List, Optional
from datetime import datetime

from models.user import User
from models.note import Note


class DataService:
     # Handles ALL data operations with JSON files
     # File management: users.json, notes.json, counters.json
    """Service for handling data persistence with JSON files."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.users_file = os.path.join(data_dir, "users.json")
        self.notes_file = os.path.join(data_dir, "notes.json")
        self.counters_file = os.path.join(data_dir, "counters.json")
        
        # Create data directory if it doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self):
        """Initialize JSON files if they don't exist."""
        if not os.path.exists(self.users_file):
            with open(self.users_file, 'w') as f:
                json.dump({}, f)
        
        if not os.path.exists(self.notes_file):
            with open(self.notes_file, 'w') as f:
                json.dump({}, f)
        
        if not os.path.exists(self.counters_file):
            with open(self.counters_file, 'w') as f:
                json.dump({"user_id_counter": 0, "note_id_counter": 0}, f)
    
    def _load_json(self, file_path: str) -> dict:
        """Load JSON data from file."""
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def _save_json(self, file_path: str, data: dict):
        """Save data to JSON file."""
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    # ID Management - ensures unique IDs for users and notes
    def get_next_user_id(self) -> int:
        """Get the next available user ID."""
        counters = self._load_json(self.counters_file)
        counters["user_id_counter"] += 1
        self._save_json(self.counters_file, counters)
        return counters["user_id_counter"]
    
    def get_next_note_id(self) -> int:
        """Get the next available note ID."""
        counters = self._load_json(self.counters_file)
        counters["note_id_counter"] += 1
        self._save_json(self.counters_file, counters)
        return counters["note_id_counter"]
    
    # User CRUD operations - Create, Read, Update, Delete
    def save_user(self, user: User) -> User:
        """Save a user to the database."""
        users = self._load_json(self.users_file)
        users[str(user.id)] = user.to_dict()
        self._save_json(self.users_file, users)
        return user
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get a user by ID."""
        users = self._load_json(self.users_file)
        user_data = users.get(str(user_id))
        return User.from_dict(user_data) if user_data else None
    
    def get_user_by_name(self, name: str) -> Optional[User]:
        """Get a user by name."""
        users = self._load_json(self.users_file)
        for user_data in users.values():
            if user_data['name'].lower() == name.lower():
                return User.from_dict(user_data)
        return None
    
    def get_all_users(self) -> List[User]:
        """Get all users."""
        users = self._load_json(self.users_file)
        return [User.from_dict(user_data) for user_data in users.values()]
    
    def delete_user(self, user_id: int) -> bool:
        """Delete a user by ID."""
        users = self._load_json(self.users_file)
        if str(user_id) in users:
            del users[str(user_id)]
            self._save_json(self.users_file, users)
            # Also delete user's notes
            self.delete_notes_by_user(user_id)
            return True
        return False
    
    # Note CRUD operations - Create, Read, Update, Delete
    def save_note(self, note: Note) -> Note:
        """Save a note to the database."""
        notes = self._load_json(self.notes_file)
        notes[str(note.id)] = note.to_dict()
        self._save_json(self.notes_file, notes)
        return note
    
    def get_note_by_id(self, note_id: int) -> Optional[Note]:
        """Get a note by ID."""
        notes = self._load_json(self.notes_file)
        note_data = notes.get(str(note_id))
        return Note.from_dict(note_data) if note_data else None
    
    def get_notes_by_user(self, user_id: int) -> List[Note]:
        """Get all notes for a specific user."""
        notes = self._load_json(self.notes_file)
        user_notes = []
        for note_data in notes.values():
            if note_data.get('user_id') == user_id:
                user_notes.append(Note.from_dict(note_data))
        return sorted(user_notes, key=lambda x: x.created_at, reverse=True)
    
    def get_all_notes(self) -> List[Note]:
        """Get all notes."""
        notes = self._load_json(self.notes_file)
        return [Note.from_dict(note_data) for note_data in notes.values()]
    
    def delete_note(self, note_id: int) -> bool:
        """Delete a note by ID."""
        notes = self._load_json(self.notes_file)
        if str(note_id) in notes:
            del notes[str(note_id)]
            self._save_json(self.notes_file, notes)
            return True
        return False
    
    def delete_notes_by_user(self, user_id: int) -> int:
        """Delete all notes for a specific user. Returns count of deleted notes."""
        notes = self._load_json(self.notes_file)
        deleted_count = 0
        notes_to_delete = []
        
        for note_id, note_data in notes.items():
            if note_data.get('user_id') == user_id:
                notes_to_delete.append(note_id)
        
        for note_id in notes_to_delete:
            del notes[note_id]
            deleted_count += 1
        
        if deleted_count > 0:
            self._save_json(self.notes_file, notes)
        
        return deleted_count 