from enum import Enum
from typing import List
from typing_extensions import Self

class ItemTypeFieldTextType(str, Enum):
    ATTACHMENT = 'ATTACHMENT'
    KEY = 'KEY' 
    RICHTEXT = 'RICHTEXT'
    TEXTAREA = 'TEXTAREA'

class ItemTypeFieldType(str, Enum):
    ACTIONS = 'ACTIONS'
    BOOLEAN = 'BOOLEAN'
    CALCULATED = 'CALCULATED'
    DATE = 'DATE'
    DOCUMENT_TYPE = 'DOCUMENT_TYPE'
    DOCUMENT_TYPE_CATEGORY_ITEM_LOOKUP = 'DOCUMENT_TYPE_CATEGORY_ITEM_LOOKUP'
    DOCUMENT_TYPE_ITEM_LOOKUP = 'DOCUMENT_TYPE_ITEM_LOOKUP'
    GROUP = 'GROUP'
    INTEGER = 'INTEGER'
    LOOKUP = 'LOOKUP'
    MULTI_LOOKUP = 'MULTI_LOOKUP'
    PROJECT = 'PROJECT'
    RELATIONSHIP_STATUS = 'RELATIONSHIP_STATUS'
    RELATIVE_DATE_RANGE = 'RELATIVE_DATE_RANGE'
    RELEASE = 'RELEASE'
    ROLLUP = 'ROLLUP'
    STEPS = 'STEPS'
    STRING = 'STRING'
    TEST_CASE_STATUS = 'TEST_CASE_STATUS'
    TEST_RUN_STATUS = 'TEST_RUN_STATUS'
    TEXT = 'TEXT'
    TIME = 'TIME'
    URL_STRING = 'URL_STRING'
    USER = 'USER'

class ItemTypeField:
    id: int
    name: str
    label: str
    field_type: ItemTypeFieldType
    read_only: bool
    read_only_allow_api_overwrite: bool
    required: bool
    trigger_suspect: bool
    synchronize: bool
    pick_list: int
    text_type: ItemTypeFieldTextType
    item_type: int

    def __init__(self):
        self.id = 0
        self.name = ""
        self.label = ""
        self.field_type = ItemTypeFieldType.ACTIONS
        self.read_only = False
        self.read_only_allow_api_overwrite = False
        self.required = False
        self.trigger_suspect = False
        self.synchronize = False
        self.pick_list = 0
        self.text_type = ItemTypeFieldTextType.ATTACHMENT
        self.item_type = 0

    def __eq__(self, other: Self):
        return self.id == other.id \
            and self.name == other.name \
            and self.label == other.label \
            and self.field_type == other.field_type \
            and self.read_only == other.read_only \
            and self.read_only_allow_api_overwrite == other.read_only_allow_api_overwrite \
            and self.required == other.required \
            and self.trigger_suspect == other.trigger_suspect \
            and self.synchronize == other.synchronize \
            and self.pick_list == other.pick_list \
            and self.text_type == other.text_type \
            and self.item_type == other.item_type

class ItemTypeCategory(str, Enum):
    ATTACHMENT = 'ATTACHMENT'
    COMPONENT = 'COMPONENT'
    CORE = 'CORE'
    DEFECT = 'DEFECT'
    SECTION = 'SECTION'
    SET = 'SET'
    TEST_CASE = 'TEST_CASE'
    TEST_CYCLE = 'TEST_CYCLE'
    TEST_PLAN = 'TEST_PLAN'
    TEST_RUN = 'TEST_RUN'
    TEXT = 'TEXT'

class ItemType:
    id: int
    type_key: str
    display: str
    display_plural: str
    description: str
    image: str
    category: ItemTypeCategory
    fields: List[ItemTypeField]
    system: bool

    def __init__(self):
        self.id = 0
        self.type_key = ""
        self.display = ""
        self.display_plural = ""
        self.description = ""
        self.image = ""
        self.category = ItemTypeCategory.ATTACHMENT
        self.fields = []
        self.system = False

    def __eq__(self, other: Self):
        return self.id == other.id \
            and self.type_key == other.type_key \
            and self.display == other.display \
            and self.display_plural == other.display_plural \
            and self.description == other.description \
            and self.image == other.image \
            and self.category == other.category \
            and self.fields == other.fields \
            and self.system == other.system