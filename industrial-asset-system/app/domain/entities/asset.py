from enum import Enum
from uuid import uuid4


class AssetStatus(str, Enum):
    ACTIVE = "ACTIVE"
    IN_MAINTENANCE = "IN_MAINTENANCE"
    RETIRED = "RETIRED"


class Asset:
    def __init__(self, name: str, location: str):
        self.id = str(uuid4())
        self.name = name
        self.location = location
        self.status = AssetStatus.ACTIVE

    def retire(self):
        if self.status == AssetStatus.IN_MAINTENANCE:
            raise ValueError("Cannot retire asset in maintenance state")
        self.status = AssetStatus.RETIRED