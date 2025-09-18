from typing import Optional, List
from models.user import User
from services.data_service import DataService


class UserService:
     # User-specific operations and validation
    """Service for handling user business logic."""
    
    def __init__(self, data_service: DataService):
        self.data_service = data_service
    
     # User creation with validation
    def create_user(self, name: str, surname: str, birthday: str, favorite_color: str) -> User:
        """Create a new user."""
        user_id = self.data_service.get_next_user_id()
        
        user = User(
            id=user_id,
            name=name.strip().title(),
            surname=surname.strip().title(),
            birthday=birthday,
            favorite_color=favorite_color.lower()
        )
        
        return self.data_service.save_user(user)
    
     # User lookup methods - returns a single user
    def get_user_by_name(self, name: str) -> Optional[User]:
        """Get a user by name."""
        return self.data_service.get_user_by_name(name)
    
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Get a user by ID."""
        return self.data_service.get_user_by_id(user_id)
    
    # User existence check - returns True if user exists
    def user_exists(self, name: str) -> bool:
        """Check if a user exists by name."""
        return self.get_user_by_name(name) is not None
    
    # User retrieval method - returns all users
    def get_all_users(self) -> List[User]:
        """Get all users."""
        return self.data_service.get_all_users()
    
    # User update method - updates user information
    def update_user(self, user_id: int, **kwargs) -> Optional[User]:
        """Update user information."""
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        
        # Update fields if provided
        if 'name' in kwargs:
            user.name = kwargs['name'].strip().title()
        if 'surname' in kwargs:
            user.surname = kwargs['surname'].strip().title()
        if 'birthday' in kwargs:
            user.birthday = kwargs['birthday']
        if 'favorite_color' in kwargs:
            user.favorite_color = kwargs['favorite_color'].lower()
        
        # Re-validate the user
        try:
            user.validate_name()
            user.validate_birthday()
            user.validate_color()
            return self.data_service.save_user(user)
        except ValueError as e:
            raise e
    
    # User deletion and cleanup method - deletes a user and all their notes
    def delete_user(self, user_id: int) -> bool:
        """Delete a user and all their notes."""
        return self.data_service.delete_user(user_id) 