from pydantic import BaseModel
from .enums import NotificationChannel


class NotificationRequest(BaseModel):
    user_id: int
    channels: list[NotificationChannel]
    title: str
    message: str