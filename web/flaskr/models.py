from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app, request, url_for
from . import db


class History(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def update_history(name):
        history = History.query.filter_by(name=name).first()
        if history is None:
            history = History(name=name)
            db.session.add(history)
        else:
            history.timestamp = datetime.utcnow
        db.session.commit()

    @staticmethod
    def query_history_time(name):
        history = History.query.filter_by(name=name).first()
        if history:
            return history.timestamp;
        return None