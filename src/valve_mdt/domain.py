"""复杂瓣膜介入合议的基础领域记录。"""
from dataclasses import dataclass, replace
from datetime import datetime, timezone


@dataclass(frozen=True)
class Record:
    record_id: str
    owner_id: str
    state: str = "draft"
    revision: int = 1
    created_at: str = ""

    def stamped(self) -> "Record":
        timestamp = self.created_at or datetime.now(timezone.utc).isoformat()
        return replace(self, created_at=timestamp)
