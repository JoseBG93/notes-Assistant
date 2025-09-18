import re
import time
from typing import List, Optional
from colorama import Fore, Style, init
from tabulate import tabulate

# Initialize colorama for cross-platform colored output
init(autoreset=True)


class InputValidator:
    """Class for validating user inputs."""
# Data validation functions
    @staticmethod
    def validate_name(name: str) -> bool:
        # Letters and spaces only
        """Validate that a name contains only letters and spaces."""
        return bool(name and name.replace(' ', '').isalpha())
    
    @staticmethod
    def validate_birthday(birthday: str) -> bool:
        # DD-MM-YYYY or DD/MM/YYYY format checking
        """Validate birthday format (DD-MM-YYYY or DD/MM/YYYY)."""
        pattern1 = re.compile(r'^\d{2}-\d{2}-\d{4}$')
        pattern2 = re.compile(r'^\d{2}/\d{2}/\d{4}$')
        return bool(pattern1.match(birthday) or pattern2.match(birthday))
    
    @staticmethod
    def validate_color(color: str) -> bool:
        # Predefined list of valid colors
        """Validate that color is in the accepted list."""
        valid_colors = [
            'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink',
            'brown', 'black', 'white', 'gray', 'grey', 'cyan', 'magenta'
        ]
        return color.lower() in valid_colors
    
    @staticmethod
    def get_valid_colors() -> List[str]:
        # Available colors list
        """Get list of valid colors."""
        return [
            'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink',
            'brown', 'black', 'white', 'gray', 'grey', 'cyan', 'magenta'
        ]


class DisplayHelper:
    """Class for formatting and displaying information."""
    
    @staticmethod
    def print_colored(text: str, color: str = 'white'):
        # Colored text output
        """Print colored text."""
        color_map = {
            'red': Fore.RED,
            'green': Fore.GREEN,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'cyan': Fore.CYAN,
            'magenta': Fore.MAGENTA,
            'white': Fore.WHITE
        }
        print(f"{color_map.get(color, Fore.WHITE)}{text}{Style.RESET_ALL}")
    
    @staticmethod
    def print_success(message: str):
        # Green success messages
        """Print success message in green."""
        DisplayHelper.print_colored(f"✓ {message}", 'green')
    
    @staticmethod
    def print_error(message: str):
        # Red error messages
        """Print error message in red."""
        DisplayHelper.print_colored(f"✗ {message}", 'red')
    
    @staticmethod
    def print_warning(message: str):
        # Yellow warning messages
        """Print warning message in yellow."""
        DisplayHelper.print_colored(f"⚠ {message}", 'yellow')
    
    @staticmethod
    def print_info(message: str):
        # Cyan info messages
        """Print info message in cyan."""
        DisplayHelper.print_colored(f"ℹ {message}", 'cyan')
    
    @staticmethod
    def print_separator(char: str = "─", length: int = 50):
        # Separator line
        """Print a separator line."""
        print(char * length)
    
    @staticmethod
    def print_header(title: str):
        # Formatted section headers
        """Print a formatted header."""
        DisplayHelper.print_separator("═")
        DisplayHelper.print_colored(f"  {title.upper()}  ", 'cyan')
        DisplayHelper.print_separator("═")
    
    @staticmethod
    def display_notes_table(notes: List, show_content: bool = False):
        # Tabulated notes display
        """Display notes in a formatted table."""
        if not notes:
            DisplayHelper.print_warning("No notes found.")
            return
        
        headers = ["ID", "Title", "Created", "Updated"]
        if show_content:
            headers.append("Content Preview")
        
        table_data = []
        for note in notes:
            row = [
                note.id,
                note.title[:30] + "..." if len(note.title) > 30 else note.title,
                note.created_at,
                note.updated_at or "Never"
            ]
            if show_content:
                content_preview = note.get_summary(40)
                row.append(content_preview)
            table_data.append(row)
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    @staticmethod
    def display_user_info(user):
        # Formatted user information
        """Display user information in a formatted way."""
        DisplayHelper.print_header("User Information")
        print(f"ID: {user.id}")
        print(f"Name: {user.name} {user.surname}")
        print(f"Birthday: {user.birthday}")
        print(f"Favorite Color: {user.favorite_color}")
        DisplayHelper.print_separator()


class InputHelper:
    """Class for handling user input with validation."""
    # User input handling with validation
    @staticmethod
    def get_input(prompt: str, validator=None, error_message: str = "Invalid input. Please try again.") -> str:
        # Validated text input
        """Get validated input from user."""
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                DisplayHelper.print_error("Input cannot be empty.")
                continue
            
            if validator is None or validator(user_input):
                return user_input
            
            DisplayHelper.print_error(error_message)
    
    @staticmethod
    def get_choice(prompt: str, valid_choices: List[str], case_sensitive: bool = False) -> str:
        # Multiple choice selection
        """Get a choice from a list of valid options."""
        while True:
            choice = input(prompt).strip()
            if not case_sensitive:
                choice = choice.lower()
                valid_choices = [c.lower() for c in valid_choices]
            
            if choice in valid_choices:
                return choice
            
            DisplayHelper.print_error(f"Please choose from: {', '.join(valid_choices)}")
    
    @staticmethod
    def get_yes_no(prompt: str) -> bool:
        """Get a yes/no answer from user."""
        # Boolean confirmation
        choice = InputHelper.get_choice(f"{prompt} (y/n): ", ['y', 'yes', 'n', 'no'])
        return choice in ['y', 'yes']
    
    @staticmethod
    def get_integer(prompt: str, min_val: int = None, max_val: int = None) -> int:
        # Numeric input with bounds
        """Get an integer input with optional min/max validation."""
        while True:
            try:
                value = int(input(prompt).strip())
                if min_val is not None and value < min_val:
                    DisplayHelper.print_error(f"Value must be at least {min_val}")
                    continue
                if max_val is not None and value > max_val:
                    DisplayHelper.print_error(f"Value must be at most {max_val}")
                    continue
                return value
            except ValueError:
                DisplayHelper.print_error("Please enter a valid number.")


def pause(seconds: float = 1.0):
    """Pause execution for specified seconds."""
    time.sleep(seconds)


def clear_screen():
    """Clear the terminal screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear') 