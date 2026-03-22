from app.core.errors import ConflictError, UnauthorizedError, NotFoundError
from app.core.security import verify_password, get_password_hash, create_access_token
from app.repositories.users import UserRepository
from app.schemas.auth import RegisterRequest
from app.schemas.user import UserPublic


class AuthUseCase:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    async def register(self, request: RegisterRequest) -> UserPublic:
        existing_user = await self.user_repo.get_by_email(request.email)
        if existing_user:
            raise ConflictError("User with this email already exists")
        
        password_hash = get_password_hash(request.password)
        user = await self.user_repo.create(
            email=request.email,
            password_hash=password_hash,
            role="user"
        )
        
        return UserPublic.model_validate(user)
    
    async def login(self, email: str, password: str) -> str:
        user = await self.user_repo.get_by_email(email)
        if not user or not verify_password(password, user.password_hash):
            raise UnauthorizedError("Invalid email or password")
        
        access_token = create_access_token(
            subject=user.id,
            role=user.role
        )
        
        return access_token
    
    async def get_profile(self, user_id: int) -> UserPublic:
        user = await self.user_repo.get_by_id(user_id)
        if not user:
            raise NotFoundError("User not found")
        
        return UserPublic.model_validate(user)