import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# Create the FastAPI app instance
app = FastAPI()

# --- Configuration ---
# Define the absolute path to the 'static' directory
# This ensures the path is correct regardless of where the script is run from
static_dir = os.path.join(os.path.dirname(__file__), "static")


# --- API Endpoints ---
# This is where you can add all your other API routes.
# They will not conflict with the frontend serving.
@app.get("/api/validate")
async def api_validate():
    """An example API endpoint."""
    return {"status": "ok", "message": "API is running"}


# --- Static Asset Mounting ---
# Mount the 'static' directory to the '/static' URL path.
# Any file in your 'static' folder will be available at '/static/filename'
# Example: your CSS file at 'static/css/styles.css' would be at 'http://.../static/css/styles.css'
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# --- Frontend Serving ---
# This route will serve your 'index.html' file from the static directory
# at the root URL ('/'). This should generally be the last route defined.
@app.get("/")
async def serve_frontend():
    """Serves the main index.html file."""
    return FileResponse(os.path.join(static_dir, "index.html"))

