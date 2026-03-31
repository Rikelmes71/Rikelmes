import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class UserIntegration(Base):
    __tablename__ = "user_integrations"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    outlook_connected: Mapped[bool] = mapped_column(Boolean, default=False)
    outlook_access_token_enc: Mapped[str | None] = mapped_column(String, nullable=True)
    outlook_refresh_token_enc: Mapped[str | None] = mapped_column(String, nullable=True)
    outlook_token_expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    reserve_username_enc: Mapped[str | None] = mapped_column(String, nullable=True)
    reserve_password_enc: Mapped[str | None] = mapped_column(String, nullable=True)
    spreadsheet_provider: Mapped[str | None] = mapped_column(String(20), nullable=True)
    spreadsheet_id_enc: Mapped[str | None] = mapped_column(String, nullable=True)
    spreadsheet_sheet_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
