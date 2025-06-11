from datetime import datetime
from jama_rest_client.model.lock import Lock

class LockJSONParser:

    @staticmethod
    def parse(lock_dict: dict) -> Lock:
        lock: Lock = Lock()
        lock.locked = lock_dict['locked']
        lock.last_locked_date = LockJSONParser.__parse_date_time(lock_dict['lastLockedDate'])
        lock.locked_by = lock_dict['lockedBy']

        return lock
    
    @staticmethod
    def __parse_date_time(date_time: str) -> datetime:
        return datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.000+0000')
