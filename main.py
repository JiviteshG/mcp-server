from docs_mcp import mcp as docs_mcp_server
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import contextlib

@contextlib.contextmanager
async def lifespan(app: FastAPI):
    async with docs_mcp_server.session_manager():
        yield

app = FastAPI(lifespan=lifespan)

# Allow CORS for all origins (for testing purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


def main():
    # This runs the server (stdio by default)
    mcp.run("stdio") # Run the server using standard input/output

if __name__ == "__main__":
    main()