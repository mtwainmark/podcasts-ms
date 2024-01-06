from fastapi import UploadFile
from fastapi.responses import FileResponse

from src.files.client import MinioClient
from src.config import settings


async def upload_file(
   file: UploadFile
) -> dict | None:
        client = MinioClient(
            endpoint=settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            bucket_name=settings.MINIO_BUCKET_NAME,
        )
        client.upload_file(file=file)
        return {"filename": file.filename}


async def download_file(
   file_path: str
) -> str | None:
        client = MinioClient(
            endpoint=settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY,
            bucket_name=settings.MINIO_BUCKET_NAME,
        )
        filename = file_path.split("/")[-1]
        client.download_file(
            source=filename, destination=filename
        )
        return FileResponse(path=filename, filename=filename, media_type='multipart/form-data')
