from datetime import timedelta

from authman.config import Config
from authman.util.now import now

def user_expires_at():
    return now() + timedelta(days=Config.USER_DEFAULT_EXPIRY_TIME)