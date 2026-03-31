from app.db.session import SessionLocal
from app.models.audit import AuditLog


class AuditService:
    def log(self, event_type: str, payload: dict, user_id=None, job_id=None, ip_address=None) -> None:
        db = SessionLocal()
        try:
            db.add(
                AuditLog(
                    event_type=event_type,
                    event_payload=payload,
                    user_id=user_id,
                    job_id=job_id,
                    ip_address=ip_address,
                )
            )
            db.commit()
        finally:
            db.close()
