from datetime import datetime
import pytest

from jama_rest_client.dal.parsers.json import LockJSONParser
from jama_rest_client.model.lock import Lock

from mocks.locks import LocksMocks, LOCKS_API_MOCKS
from test_utilities.builders.lock import LockBuilder

class TestLockJSONParser():

    @pytest.mark.parametrize(
      "lock_dict, expected_lock",
      [
        (
            LOCKS_API_MOCKS[LocksMocks.CASE_LOCK_LOCKED],
            LockBuilder().set_locked(True)
                         .set_last_locked_date(datetime.fromtimestamp(1582199426))
                         .set_locked_by(0)
                         .get_element()
        ),
        (
            LOCKS_API_MOCKS[LocksMocks.CASE_LOCK_NOT_LOCKED],
            LockBuilder().set_locked(False)
                         .set_last_locked_date(datetime.fromtimestamp(1582199426))
                         .set_locked_by(0)
                         .get_element()
        )
      ]
    )
    def test_validate_happy_path_parse_item_returns_expected_value(self, lock_dict: dict, expected_lock: Lock) -> None:
        lock = LockJSONParser.parse(lock_dict)
        assert expected_lock == lock