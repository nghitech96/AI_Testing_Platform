from fastapi import FastAPI

from backend.api.upload import router as upload_router
from backend.api.evaluation import router as evaluation_router
from backend.api.report import router as report_router

app = FastAPI(
    title="AI Testing Platform"
)

app.include_router(upload_router)
app.include_router(evaluation_router)
app.include_router(report_router)