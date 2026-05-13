from mcp_server import mcp

def main():
    # This runs the server (stdio by default)
    mcp.run("stdio") # Run the server using standard input/output

if __name__ == "__main__":
    main()