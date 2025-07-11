from fastapi import FastAPI  # Import the FastAPI class from the FastAPI framework

# Create the main FastAPI app instance (the core of the application)
# This object handles routing, docs, and app configuration
app = FastAPI(
    title="LumaireJ",  # App title shown in auto-generated docs
    description="A journaling app for emotional self-awareness and reflection",  # Description in docs
    version="0.1.0",  # App version
    docs_url="/api/docs",  # Swagger UI
    redoc_url="/api/redoc",  # ReDoc UI
)

@app.get("/health")  # Register a GET route at /health
def health_check() -> dict:
    """
    Health check endpoint.
    Returns a JSON response confirming the app is running and includes its version.
    """
    return {"status": "healthy", "version": app.version}