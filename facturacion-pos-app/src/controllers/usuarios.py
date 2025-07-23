from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session
from typing import List, Optional
from src.db.models import User  # Asegúrate de que el modelo User esté definido en models.py

class UserController:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, username: str, password: str, is_admin: bool = False) -> User:
        new_user = User(username=username, password=password, is_admin=is_admin)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def get_user(self, user_id: int) -> Optional[User]:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_all_users(self) -> List[User]:
        return self.session.query(User).all()

    def update_user(self, user_id: int, username: Optional[str] = None, password: Optional[str] = None, is_admin: Optional[bool] = None) -> Optional[User]:
        user = self.get_user(user_id)
        if user:
            if username is not None:
                user.username = username
            if password is not None:
                user.password = password
            if is_admin is not None:
                user.is_admin = is_admin
            self.session.commit()
            return user
        return None

    def delete_user(self, user_id: int) -> bool:
        user = self.get_user(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        return self.session.query(User).filter(User.username == username, User.password == password).first()