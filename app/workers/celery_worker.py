from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "saas_worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)

@celery_app.task(name="send_welcome_email")
def send_welcome_email(org_id: int, org_name: str):
    """
    Triggered when a new organization is created.
    Simulates sending a welcome email to the new tenant.
    """
    print(f"[EMAIL] Welcome to {org_name}!")
    print(f"[EMAIL] Org ID: {org_id}")
    print(f"[EMAIL] Your workspace is ready. Start creating projects.")
    return {
        "status": "sent",
        "org_id": org_id,
        "org_name": org_name
    }