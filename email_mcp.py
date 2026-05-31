from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("mcp-email-server")

# Email function (Internal logic)
@mcp.tool()
def get_emails() -> dict:
    """
    This tool returns a list of email from the database for the project.
    It is very useful for figuring out what the object is about. 
    """
    return {
        "title": "How to use the MCP server emails",
        "body": "This is a mocked email entry from the database. Use this as a reference for your AI agent integration.",
        "source": "mocked_email"
    }

# Register the tool
@mcp.tool()
def write_email(
    recipient: str,
    subject: str,
    body: str
) -> dict:
    """
    This tool allows you to write an email to a recipient. 
    It is very useful for figuring out what the object is about. 
    """
    # Here you would implement the logic to send an email using an email service or SMTP server.
    # For this example, we will just return a mocked response.
    return {
        "status": "success",
        "message": f"Email sent to {recipient} with subject '{subject}' and body '{body}'."
    }
