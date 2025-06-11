from datetime import datetime
from jama_rest_client.model.lock import Lock
from typing_extensions import Self

class LockBuilder:
    __lock: Lock

    def __init__(self):
        self.__lock = Lock()

    def set_locked(self, locked: bool) -> Self:
        self.__lock.locked = locked
        return self
    
    def set_last_locked_date(self, last_locked_date: datetime) -> Self:
        self.__lock.last_locked_date = last_locked_date
        return self
    
    def set_locked_by(self, locked_by: int) -> Self:
        self.__lock.locked_by = locked_by
        return self
    
    def get_element(self) -> Lock:
        return self.__lock