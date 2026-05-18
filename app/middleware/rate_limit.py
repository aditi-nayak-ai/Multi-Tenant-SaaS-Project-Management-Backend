import time
import redis
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


redis_client = redis.Redis(host="localhost", port=6379, db=0)


class RateLimitMiddleware(BaseHTTPMiddleware):

    RATE_LIMIT = 100
    WINDOW = 60

    async def dispatch(self, request: Request, call_next):

        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"

        current = redis_client.get(key)

        if current and int(current) >= self.RATE_LIMIT:
            return JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded"}
            )

        pipe = redis_client.pipeline()
        pipe.incr(key, 1)
        pipe.expire(key, self.WINDOW)
        pipe.execute()

        response = await call_next(request)

        return response
