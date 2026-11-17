from flask import jsonify
from .. import db
from . import health_bp

@health_bp.route("/health")
def health():
    try:
        # AÑADIDO db.text() para que SQLAlchemy no se queje
        db.session.execute(db.text("SELECT 1"))
        return jsonify({"status": "ok", "database": "ok"}), 200
    except Exception:
        return jsonify({"status": "error", "database": "error"}), 503