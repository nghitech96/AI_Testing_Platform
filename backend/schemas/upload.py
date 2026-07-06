from pydantic import BaseModel, Field


class UploadResponse(BaseModel):
    success: bool = Field(
        ...,
        description="Upload status"
    )

    message: str = Field(
        ...,
        description="Response message"
    )

    filename: str = Field(
        ...,
        description="Uploaded file name"
    )

    rows: int = Field(
        ...,
        description="Number of rows in dataset"
    )

    columns: list[str] = Field(
        ...,
        description="List of column names"
    )
    
    file_size: float = Field(
        ...,
        description="File size in MB"
    )