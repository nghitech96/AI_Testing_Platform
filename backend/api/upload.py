from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import shutil
import pandas as pd
from backend.schemas.upload import UploadResponse

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_FOLDER = "datasets"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/")
async def upload_dataset(file: UploadFile = File(...)):
    """
    Upload dataset CSV
    """

    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed."
        )

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = pd.read_csv(file_path)

    return UploadResponse(
        success=True,
        message="Upload successful",
        filename=file.filename,
        file_size=round(os.path.getsize(file_path) / 1024, 2),
        rows=len(df),
        columns=df.columns.tolist() 
    )
    