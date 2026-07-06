from pydantic import BaseModel


class UploadResponse(BaseModel):
    success: bool
    message: str
    filename: str
    file_size: float
    rows: int