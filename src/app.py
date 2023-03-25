from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from prisma import Prisma
from src.routers import user


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connects to the prisma query engine before app starts."""
    await db.connect()

    yield
    # Clean up connections when the server shuts down."""
    await db.disconnect()

app = FastAPI(title="BetterEd", lifespan=lifespan)
db = Prisma(auto_register=True)
app.include_router(user.router)

# Allow all origins, all headers except Authorization and all request methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def ping() -> dict[str, str]:
    """API Ping endpoint."""
    return {"message": "Pong!"}