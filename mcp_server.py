from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Mocked Documentation Server")

# Mocked database function (Internal logic)
def get_mocked_documentation():
    return {
        "id": 1,
        "title": "How to use the MCP server",
        "content": "This is a mocked documentation entry from the database. Use this as a reference for your AI agent integration.",
        "tags": ["mcp", "documentation", "example"]
    }

# Register the tool
@mcp.tool()
def get_documentation_from_database() -> dict:
    """Return documentation data from the database."""
    return get_mocked_documentation()

if __name__ == "__main__":
    mcp.run("stdio")  # Run the server using standard input/output