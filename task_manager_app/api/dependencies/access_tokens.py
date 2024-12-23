from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from core.models import db_runner, User, AccessToken


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_access_token_db(session: Annotated[AsyncSession, Depends(db_runner.session_getter)]):
    yield AccessToken.get_db(session=session)