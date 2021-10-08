from authman.authman import db
from authman.config import Config
from authman.util import uuidgen,now,user_expires_at
class User(db.Model):
    id = db.Column(db.String(64),primary_key=True,default=uuidgen) 
    """
    if use uuidgen() it called function and get string once ,you must use uuidgen 
     to use it refrence and generate every time.
    """
    username = db.Column(db.String(128), unique=True,index=True)
    password = db.Column(db.String(256),nullable=False)
    role = db.Column(db.String(32),nullable=False,default=Config.USER_DEFAULT_ROLE)
    created_at = db.Column(db.DateTime,nullable=False,default=now)
    expires_at = db.Column(db.DateTime,nullable=False,default=user_expires_at)
    last_login_at = db.Column(db.DateTime)
    last_active_at = db.Column(db.DateTime)
    last_change_at = db.Column(db.DateTime)
    failed_auth_at = db.Column(db.DateTime)
    failed_auth_count = db.Column(db.Integer,nullable=False,default=3)
    status = db.Column(db.Integer,nullable=False,default=Config.USER_DEFAULT_STATUS)
