from fastapi_users import FastAPIUsers

from api.dependencies.backend import auth_backend
from api.dependencies.user_manager import get_user_manager
from core.models import User
from core.types import UserIdType

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend],
)