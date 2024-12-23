import logging
from typing import Optional, TYPE_CHECKING

from fastapi_users import BaseUserManager, IntegerIDMixin

from core.models import User
from core.types import UserIdType

if TYPE_CHECKING:
    from fastapi import Request


SECRET = "" # TODO

log = logging.getLogger(__name__)


class UserManager(IntegerIDMixin, BaseUserManager[User, UserIdType]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET



    async def on_after_register(self, user: User, request: Optional[Request] = None):
        log.warning("User %r has registered.",user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)
