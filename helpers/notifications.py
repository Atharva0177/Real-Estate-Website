import traceback
from flask import current_app
from flask_mail import Message
from models import db, ActivityLog

def log_activity(action, description, actor_type='system', actor_id=None):
    try:
        act = ActivityLog(
            action=action,
            description=description,
            actor_type=actor_type,
            actor_id=actor_id
        )
        db.session.add(act)
        db.session.commit()
    except Exception:
        db.session.rollback()

def send_email(mail, subject, recipients, body, html=None, category='system'):
    """
    Safe email sender; logs success/failure to ActivityLog.
    """
    if not mail:
        current_app.logger.warning("Mail instance not initialized.")
        return False
    if not recipients:
        return False
    if isinstance(recipients, str):
        recipients = [recipients]

    if not current_app.config.get('MAIL_USERNAME') or not current_app.config.get('MAIL_PASSWORD'):
        current_app.logger.warning("Email skipped: MAIL_USERNAME / MAIL_PASSWORD not configured.")
        log_activity('email_skipped', f'Email skipped (missing credentials): {subject}', 'system')
        return False

    try:
        msg = Message(subject=subject, recipients=recipients, body=body, html=html)
        mail.send(msg)
        log_activity(f'email_{category}', f"Email sent: {subject}", 'system')
        return True
    except Exception as e:
        tb = traceback.format_exc()
        current_app.logger.error(f"Email send failed: {e}\n{tb}")
        log_activity('email_error', f"Email failed: {subject} - {e}", 'system')
        return False