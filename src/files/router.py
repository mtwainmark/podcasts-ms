from fastapi import APIRouter, Depends, status
from fastapi.background import BackgroundTasks
from fastapi.responses import FileResponse

from src.files.schemas import FileDownload, FileUpload, FileUploadResponse
from src.files.services import download_file, upload_file
from src.exceptions import NotAuthenticated, NotFound

file_router = APIRouter(prefix="/files", tags=["files"])


@file_router.post(
    "/",
    response_model=FileUploadResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["files"],
)
async def file_upload(file: FileUpload = Depends()):
    if uploaded := await upload_file(
       file=file.file
    ):
        return uploaded


@file_router.get(
    "/",
    response_class=FileResponse,
    tags=["files"],
)
async def file_download(
    file: FileDownload = Depends(),
):
    return await download_file(
       file_path=file.file_path
    )