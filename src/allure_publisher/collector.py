import io
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


def collect_files(directory: Path):
    """Создать архив с файлами из указанной директории"""
    buffer = io.BytesIO()

    with ZipFile(buffer, mode='w', compression=ZIP_DEFLATED) as archive:
        _pack_files(archive, directory)

    buffer.seek(0)
    return buffer


def _pack_files(archive: ZipFile, dir_path: Path):
    """Упаковать все файлы директории в архив"""
    for item in dir_path.iterdir():
        if not item.is_file():
            continue

        archive.write(item, item.name, compress_type=ZIP_DEFLATED)
