from os import fstat, path, remove

from fastapi import Form, UploadFile

def file_size(file: UploadFile) -> int:
    return fstat(file.file.fileno()).st_size
