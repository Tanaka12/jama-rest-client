from datetime import datetime
from jama_rest_client.model.lock import Lock

class LockJSONParser:

    @staticmethod
    def parse(lock_dict: dict) -> Lock:
        lock: Lock = Lock()
        lock.locked = lock_dict['locked']
        lock.last_locked_date = datetime.fromisoformat(lock_dict['lastLockedDate'])
        lock.locked_by = lock_dict['lockedBy']

        return lock
