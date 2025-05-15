import json
from typing import Annotated
from fastmcp import FastMCP
from pydantic import Field

from .users import load_workday_users

mcp = FastMCP(name="Workday MCP Service",
              description="Provides tools for interacting with Workday.",
              )


@mcp.tool()
async def get_user_quarter_goal(
        user_identifier: Annotated[
            str,
            Field(
                description="Identifier for the user (e.g., email address 'user@example.com', username 'johndoe', "
                            "account ID 'accountid:...', or key for Server/DC)."
            ),
        ],
) -> str:
    """
    Retrieve Quarter goals for specific Workday user.

    Args:
        user_identifier: User identifier (email, username, key, or account ID).

    Returns:
        JSON string representing the Workday user quarter goal object, or an error object if not found.

    Raises:
        ValueError: If the Workday client is not configured or available.
    """

    users = load_workday_users()
    response_data = ""
    for user in users:
        if user.email == user_identifier:
            if user.quarter_goals:
                goals_str = "\n".join(f"{question}: {answer}" for question, answer in user.quarter_goals.items())
                quarter_goals = f"Quarterly Goals for {user.display_name}:\n{goals_str}"
                response_data = {"success": True, "user": quarter_goals}
            else:
                response_data = f"{user.display_name} has no quarterly goals set."

    return json.dumps(response_data, indent=2, ensure_ascii=False)
