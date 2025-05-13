import json
from pathlib import Path
from typing import Any, Dict, List

from pydantic import BaseModel, Field


class WorkdayUser(BaseModel):
    """
    Model representing a Workday user.
    """

    account_id: str | None = None
    display_name: str = "Unassigned"
    email: str | None = None
    active: bool = True
    avatar_url: str | None = None
    time_zone: str | None = None
    quarter_goals: Dict[str, Any] = Field(default_factory=dict)


# Function to load JSON and create instances
def load_workday_users() -> List[WorkdayUser]:
    """
    Load WorkdayUser instances from a JSON file located in the same directory
    as this Python file.
    """
    current_dir = Path(__file__).parent
    json_file = current_dir / "workday_users.json"

    with json_file.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return [WorkdayUser(**item) for item in data]