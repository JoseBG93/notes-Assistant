#!/usr/bin/env python3
"""
Notes Assistant - A simple CRUD application for managing personal notes.
"""

import sys
import os
from typing import Optional
# Import new dependencies from requirements.txt
import click
import rich
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live
from rich.layout import Layout
from rich.align import Align
from rich.columns import Columns
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.tree import Tree
from rich.traceback import install as install_rich_traceback
from rich import print as rprint
import questionary
from questionary import Style
import pyfiglet
from alive_progress import alive_bar
import time

# Initialize rich console
console = Console()

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.user import User
from models.note import Note
from services.data_service import DataService
from services.user_service import UserService
from services.notes_service import NotesService
from utils.helpers import (
    InputValidator, DisplayHelper, InputHelper, 
    pause, clear_screen
)


class NotesAssistantApp:
    """Main application class for the Notes Assistant."""
    # Central orchestrator - coordinates all components
    # Handles: Authentication, Menu system, User interactions
    # Dependencies: All models + services + utils
    
    def __init__(self):
        # Use the data directory relative to this source file
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        self.data_service = DataService(data_dir)
        self.user_service = UserService(self.data_service)
        self.notes_service = NotesService(self.data_service)
        self.current_user: Optional[User] = None
    
    def run(self):
        """Main application loop."""
        # Use rich instead of DisplayHelper
        console.print(Panel.fit("🗒️  Welcome to Notes Assistant", style="bold blue"))
        console.print("✨ Your personal notes management system", style="italic cyan")
        pause(1)
        
        # Authentication
        if not self.authenticate():
            console.print("👋 Goodbye!", style="yellow")
            return
        
        # Main menu loop
        while True:
            try:
                self.show_main_menu()
                choice = questionary.select(
                    "What would you like to do?",
                    choices=[
                        "Create a new note",
                        "Read a note", 
                        "Update a note",
                        "Delete a note",
                        "Search notes",
                        "List all notes",
                        "Show user info",
                        "Exit"
                    ]
                ).ask()
                
                if choice == "Create a new note":
                    self.create_note()
                elif choice == "Read a note":
                    self.read_note()
                elif choice == "Update a note":
                    self.update_note()
                elif choice == "Delete a note":
                    self.delete_note()
                elif choice == "Search notes":
                    self.search_notes()
                elif choice == "List all notes":
                    self.list_notes()
                elif choice == "Show user info":
                    self.show_user_info()
                elif choice == "Exit":
                    break
                
                pause(1)
                
            except KeyboardInterrupt:
                console.print("\n⚠️  Operation cancelled.", style="yellow")
                pause(1)
            except Exception as e:
                console.print(f"❌ An error occurred: {str(e)}", style="red")
                pause(2)
        
        console.print("🎉 Thanks for using Notes Assistant. Goodbye!", style="green bold")
    
    def authenticate(self) -> bool:
        """Handle user authentication or registration."""
        console.print(Panel("🔐 Authentication", style="bold magenta"))
        
        name = questionary.text("Please enter your name:").ask()
        
        if not InputValidator.validate_name(name):
            console.print("❌ Name must contain only letters and spaces.", style="red")
            return False
        
        user = self.user_service.get_user_by_name(name)
        
        if user:
            console.print(f"✅ Welcome back, {user.name}!", style="green")
            self.current_user = user
            return True
        else:
            console.print("⚠️  You're not registered yet.", style="yellow")
            if questionary.confirm("Would you like to create an account?").ask():
                return self.register_user(name)
            else:
                return False
    
    def register_user(self, name: str) -> bool:
        """Register a new user."""
        try:
            console.print(Panel("📝 User Registration", style="bold blue"))
            console.print("Please provide some additional information:", style="cyan")
            
            surname = questionary.text("Surname:").ask()
            if not InputValidator.validate_name(surname):
                console.print("❌ Surname must contain only letters and spaces.", style="red")
                return False
            
            birthday = questionary.text("Birthday (DD-MM-YYYY or DD/MM/YYYY):").ask()
            if not InputValidator.validate_birthday(birthday):
                console.print("❌ Please use DD-MM-YYYY or DD/MM/YYYY format.", style="red")
                return False
            
            valid_colors = InputValidator.get_valid_colors()
            favorite_color = questionary.select(
                "Choose your favorite color:",
                choices=valid_colors
            ).ask()
            
            user = self.user_service.create_user(name, surname, birthday, favorite_color)
            self.current_user = user
            
            console.print("✅ Account created successfully!", style="green bold")
            self.display_user_info_rich(user)
            pause(2)
            return True
            
        except ValueError as e:
            console.print(f"❌ Registration failed: {str(e)}", style="red")
            return False
    
    def show_main_menu(self):
        """Display the main menu."""
        clear_screen()
        
        # Create ASCII art header with pyfiglet
        title = pyfiglet.figlet_format("Notes App", font="slant")
        console.print(title, style="bold blue")
        
        console.print(f"👤 User: {self.current_user.name}", style="cyan")
        
        summary = self.notes_service.get_notes_summary(self.current_user.id)
        console.print(f"📝 You have {summary['total_notes']} notes", style="green")
    
    def display_user_info_rich(self, user):
        """Display user information using rich formatting."""
        table = Table(title="👤 User Information")
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")
        
        table.add_row("ID", str(user.id))
        table.add_row("Name", f"{user.name} {user.surname}")
        table.add_row("Birthday", user.birthday)
        table.add_row("Favorite Color", user.favorite_color)
        
        console.print(table)
    
    def display_notes_table_rich(self, notes, show_content: bool = False):
        """Display notes in a beautiful rich table."""
        if not notes:
            console.print("⚠️  No notes found.", style="yellow")
            return
        
        table = Table(title="📝 Your Notes")
        table.add_column("ID", style="cyan", justify="center")
        table.add_column("Title", style="magenta")
        table.add_column("Created", style="green")
        table.add_column("Updated", style="yellow")
        
        if show_content:
            table.add_column("Content Preview", style="white")
        
        for note in notes:
            title = note.title[:30] + "..." if len(note.title) > 30 else note.title
            updated = note.updated_at or "Never"
            
            row = [
                str(note.id),
                title,
                note.created_at,
                updated
            ]
            
            if show_content:
                content_preview = note.get_summary(40)
                row.append(content_preview)
            
            table.add_row(*row)
        
        console.print(table)
    
    def create_note(self):
        """Create a new note."""
        console.print(Panel("🖊️ Create New Note", style="bold blue"))
        
        title = questionary.text("Note title:").ask()
        console.print("Note content (press Enter twice to finish):", style="cyan")
        
        content_lines = []
        while True:
            line = input()
            if line == "" and content_lines and content_lines[-1] == "":
                break
            content_lines.append(line)
        
        content = "\n".join(content_lines).strip()
        if not content:
            console.print("❌ Note content cannot be empty.", style="red")
            return
        
        try:
            note = self.notes_service.create_note(title, content, self.current_user.id)
            console.print(f"✅ Note '{note.title}' created successfully!", style="green bold")
            console.print(f"📝 Note ID: {note.id}", style="cyan")
            console.print(f"📅 Created: {note.created_at}", style="cyan")
        except ValueError as e:
            console.print(f"❌ Failed to create note: {str(e)}", style="red")
    
    def read_note(self):
        """Read a specific note."""
        notes = self.notes_service.get_user_notes(self.current_user.id)
        if not notes:
            console.print("⚠️  You don't have any notes yet.", style="yellow")
            return
        
        console.print(Panel("📚 Your Notes", style="bold blue"))
        self.display_notes_table_rich(notes)
        
        try:
            note_id = int(questionary.text("Enter note ID to read:").ask())
            note = self.notes_service.get_note(note_id, self.current_user.id)
            
            if note:
                console.print(Panel(f"📝 Note: {note.title}", style="bold magenta"))
                console.print(f"📝 ID: {note.id}", style="cyan")
                console.print(f"📅 Created: {note.created_at}", style="cyan")
                if note.updated_at:
                    console.print(f"📅 Updated: {note.updated_at}", style="cyan")
                console.rule()
                console.print(note.content)
                console.rule()
                
                input("\nPress Enter to continue...")
            else:
                console.print("❌ Note not found or doesn't belong to you.", style="red")
                
        except (ValueError, TypeError):
            console.print("❌ Invalid note ID.", style="red")
    
    def update_note(self):
        """Update an existing note."""
        notes = self.notes_service.get_user_notes(self.current_user.id)
        if not notes:
            console.print("⚠️  You don't have any notes yet.", style="yellow")
            return
        
        console.print(Panel("📝 Update Note", style="bold blue"))
        self.display_notes_table_rich(notes)
        
        try:
            note_id = int(questionary.text("Enter note ID to update:").ask())
            note = self.notes_service.get_note(note_id, self.current_user.id)
            
            if not note:
                console.print("❌ Note not found or doesn't belong to you.", style="red")
                return
            
            update_choice = questionary.select(
                "What would you like to update?",
                choices=['Title', 'Content', 'Both']
            ).ask()
            
            if update_choice in ['Title', 'Both']:
                new_title = questionary.text(f"New title (current: {note.title}):").ask()
                self.notes_service.update_note_title(note_id, new_title, self.current_user.id)
                console.print("✅ Title updated successfully!", style="green bold")
            
            if update_choice in ['Content', 'Both']:
                console.print("Enter new content (press Enter twice to finish):", style="cyan")
                content_lines = []
                while True:
                    line = input()
                    if line == "" and content_lines and content_lines[-1] == "":
                        break
                    content_lines.append(line)
                
                new_content = "\n".join(content_lines).strip()
                if new_content:
                    self.notes_service.update_note_content(note_id, new_content, self.current_user.id)
                    console.print("✅ Content updated successfully!", style="green bold")
                else:
                    console.print("❌ Content cannot be empty.", style="red")
                    
        except (ValueError, TypeError) as e:
            console.print(f"❌ Update failed: {str(e)}", style="red")
    
    def delete_note(self):
        """Delete a note."""
        notes = self.notes_service.get_user_notes(self.current_user.id)
        if not notes:
            console.print("⚠️  You don't have any notes yet.", style="yellow")
            return
        
        console.print(Panel("❌ Delete Note", style="bold red"))
        self.display_notes_table_rich(notes)
        
        try:
            note_id = int(questionary.text("Enter note ID to delete:").ask())
            note = self.notes_service.get_note(note_id, self.current_user.id)
            
            if not note:
                console.print("❌ Note not found or doesn't belong to you.", style="red")
                return
            
            console.print(Panel(f"❌ You are about to delete: '{note.title}'", style="bold red"))
            if questionary.confirm("Are you sure?").ask():
                if self.notes_service.delete_note(note_id, self.current_user.id):
                    console.print("✅ Note deleted successfully!", style="green bold")
                else:
                    console.print("❌ Failed to delete note.", style="red")
            else:
                console.print("✅ Deletion cancelled.", style="green")
                
        except (ValueError, TypeError):
            console.print("❌ Invalid note ID.", style="red")
    
    def search_notes(self):
        """Search notes by title or content."""
        console.print(Panel("🔍 Search Notes", style="bold blue"))
        
        query = questionary.text("Enter search term:").ask()
        results = self.notes_service.search_notes(query, self.current_user.id)
        
        if results:
            console.print(f"✅ Found {len(results)} note(s):", style="green")
            self.display_notes_table_rich(results, show_content=True)
        else:
            console.print("⚠️  No notes found matching your search.", style="yellow")
        
        input("\nPress Enter to continue...")
    
    def list_notes(self):
        """List all user notes."""
        console.print(Panel("📋 All Notes", style="bold blue"))
        
        notes = self.notes_service.get_user_notes(self.current_user.id)
        self.display_notes_table_rich(notes, show_content=True)
        
        input("\nPress Enter to continue...")
    
    def show_user_info(self):
        """Show current user information."""
        self.display_user_info_rich(self.current_user)
        
        summary = self.notes_service.get_notes_summary(self.current_user.id)
        console.print(f"📝 Total notes: {summary['total_notes']}", style="cyan")
        
        if summary['newest_note']:
            console.print(f"📅 Newest note: '{summary['newest_note'].title}' ({summary['newest_note'].created_at})", style="cyan")
        
        if summary['oldest_note']:
            console.print(f"📅 Oldest note: '{summary['oldest_note'].title}' ({summary['oldest_note'].created_at})", style="cyan")
        
        input("\nPress Enter to continue...")


def main(): # This function is called from the run.py file ("from main import main"), to start the application.
    """Entry point of the application."""
    try:
        app = NotesAssistantApp() # Create an instance of the NotesAssistantApp class.
        app.run() # Run the application, by calling the run() method of the NotesAssistantApp class.
    except KeyboardInterrupt:
        console.print("\n\nApplication terminated by user.", style="yellow") # Print a message to the console, when the user presses Ctrl+C.
    except Exception as e:
        console.print(f"\n❌ Fatal error: {str(e)}", style="red") # Print a message to the console, when an error occurs.
        console.print("Please check your installation and try again.", style="yellow")


if __name__ == "__main__":
    main() 