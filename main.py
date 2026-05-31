from docs_mcp import mcp as docs_mcp_server
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
import contextlib
import uvicorn

@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with docs_mcp_server.session_manager.run():
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


app.mount("/docs", docs_mcp_server.streamable_http_app())

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=10000, log_level="debug")