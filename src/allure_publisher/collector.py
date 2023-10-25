import io
from concurrent.futures import ThreadPoolExecutor, wait
from pathlib import Path
from zipfile import ZipFile


def collect_files(directory: Path):
    """Создать архив с файлами из указанной директории"""
    buffer = io.BytesIO()

    with ZipFile(buffer, mode='w') as archive:
        _pack_files(archive, directory)

    buffer.seek(0)
    return buffer


def _pack_files(archive: ZipFile, dir_path: Path):
    """Упаковать все файлы директории в архив"""
    with ThreadPoolExecutor() as executor:
        files = [item for item in dir_path.iterdir() if item.is_file()]
        futures = [executor.submit(_pack_file, archive, file) for file in files]
        wait(futures)


def _pack_file(archive: ZipFile, file_path: Path):
    """Упаковать файл в архив"""
    with open(file_path, 'rb') as f:
        archive.writestr(file_path.name, f.read())
