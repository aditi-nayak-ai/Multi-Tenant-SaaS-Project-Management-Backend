from fastapi import Request
from jose import jwt
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings


class TenantMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        auth_header = request.headers.get("Authorization")

        request.state.organization_id = None

        if auth_header and auth_header.startswith("Bearer "):

            token = auth_header.split(" ")[1]

            try:
                payload = jwt.decode(
                    token,
                    settings.SECRET_KEY,
                    algorithms=[settings.ALGORITHM]
                )

                request.state.organization_id = payload.get("organization_id")

            except Exception:
                pass

        response = await call_next(request)

        return response
