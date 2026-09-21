"""MCP Server for Google Gemini via browser cookies."""

import utils.net
import utils.clients
import utils.http_session
import utils.transport
import utils.session
from gemini_webapi_mcp.server import mcp


def main():
    """Entry point for the gemini-webapi-mcp command."""
    mcp.run()
