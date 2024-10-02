# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the EmailerWorker project.

import os
import sys
import uuid
from typing import Optional

from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi_health import health
from starlette.middleware.base import BaseHTTPMiddleware

from src.api.v1.prompt_router import router as prompt_router
from src.core.config import settings
from src.core.context import request_id_context

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Custom security scheme for JWT
security = HTTPBasic()


def verify_credentials(credentials: HTTPBasicCredentials):
    """Check if the provided username and password are correct."""
    api_username = settings.BASIC_AUTH_USERNAME
    api_password = settings.BASIC_AUTH_PASSWORD

    if not (credentials.username == api_username and credentials.password == api_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


def auth_dependency(credentials: Optional[HTTPBasicCredentials] = Depends(security)):
    """Dependency function for Basic Auth."""
    if credentials:
        verify_credentials(credentials)


app = FastAPI(
    title="Ask Docs Server APIs",
    description="APIs for GPT-powered system for answering questions from internal documents.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)


# Middleware for generating and adding request ID
class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get the request ID from headers, or generate one
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request_id_context.set(request_id)

        # Continue processing the request
        response = await call_next(request)

        # Attach the request ID to the response headers
        response.headers["X-Request-ID"] = request_id
        return response


async def health_check():
    return {"status": "healthy"}


# Add the middleware
app.add_middleware(RequestIDMiddleware)

# Include routers
app.add_api_route("/health", health([health_check]), tags=["Management"], description="Management APIs")

app.include_router(prompt_router, prefix="/api/v1/prompt", tags=["Prompt Operations"],
                   dependencies=[Depends(auth_dependency)])


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ask Docs Server APIs",
        version="1.0.0",
        description="APIs for GPT-powered system for answering questions from internal documents.",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


@app.on_event("startup")
async def startup_db_client():
    pass


@app.on_event("shutdown")
async def shutdown_db_client():
    # await close_mongo_connection()
    pass


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
