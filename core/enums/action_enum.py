from enum import Enum
from datetime import timedelta


class ActionEnum(Enum):
    ACTIVATE = ('activate', timedelta(days=1))
    RECOVER_PASSWORD = ('recover', timedelta(days=1))

    def __init__(self, token_type, exp_time):
        self.token_type = token_type
        self.exp_time = exp_time
