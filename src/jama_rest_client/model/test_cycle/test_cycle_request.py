from enum import Enum
from typing import List
from typing_extensions import Self

class TestRunStatus(str, Enum):
    PASSED = 'PASSED'
    NOT_RUN = 'NOT_RUN'
    IN_PROGRESS = 'INPROGRESS'
    FAILED = 'FAILED'
    BLOCKED = 'BLOCKED'

class TestRunGenerationConfig:
    test_groups_to_include: List[int]
    test_run_statuses_to_include: List[TestRunStatus]

    def __init__(self):
        self.test_groups_to_include = []
        self.test_run_statuses_to_include = []

    def __eq__(self, other: Self):
        return self.test_groups_to_include == other.test_groups_to_include \
            and self.test_run_statuses_to_include == other.test_run_statuses_to_include

class TestCycleRequest:
    test_run_generation_config: TestRunGenerationConfig
    fields: dict

    def __init__(self):
        self.test_run_generation_config = TestRunGenerationConfig()
        self.fields = {}

    def __eq__(self, other: Self):
        return self.test_run_generation_config == other.test_run_generation_config \
            and self.fields == other.fields
