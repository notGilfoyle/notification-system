from uuid import uuid4

from pydantic import BaseModel, Field

from .enums import NotificationChannel, NotificationStatus


class NotificationJob(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))

    user_id: int

    channel: NotificationChannel

    title: str

    message: str

    status: NotificationStatus = NotificationStatus.PENDING

    retry_count: int = 0