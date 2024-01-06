from bson import ObjectId
from fastapi import UploadFile
from pydantic import BaseModel


class FileDownload(BaseModel):
    file_path: str


class FileUpload(BaseModel):
    file: UploadFile


class FileUploadResponse(BaseModel):
    filename: str

    class Config:
        json_encoders = {ObjectId: str}