import os
from dotenv import find_dotenv, load_dotenv
from .workday import mcp

# Load environment variables from .env file
load_dotenv(find_dotenv())


def start_app():
    """Function to start the Flask application."""
    print("Starting Workday MCP Server Flask app")
    port = int(os.environ.get("PORT", "8080"))
    mcp.run(transport="sse", host="0.0.0.0", port=port)


if __name__ == "__main__":
    start_app()
