from starlette.middleware.base import BaseHTTPMiddleware
import time
import logging

logger = logging.getLogger("saas.request")
logging.basicConfig(level=logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = round((time.time() - start) * 1000, 2)

        org_id = getattr(request.state, "organization_id", None)

        logger.info(
            f"{request.method} {request.url.path} "
            f"status={response.status_code} "
            f"org={org_id} "
            f"duration={duration}ms"
        )

        return response