from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)

REPORT_FOLDER = "reports"

@router.get("/{filename}")
def download_report(filename: str):
    file_path = os.path.join(REPORT_FOLDER, filename)
    path = os.path.join(
        REPORT_FOLDER,
        filename
    )

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail=f"Report '{filename}' not found."
        )

    return FileResponse(
        path,
        media_type="application/octet-stream",
        filename=filename
    )