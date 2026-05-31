from docs_mcp import mcp as docs_mcp_server
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def main():
    # This runs the server (stdio by default)
    mcp.run("stdio") # Run the server using standard input/output

if __name__ == "__main__":
    main()