from pathlib import Path

def validate_file_path(path: str) -> Path:
    file_path = Path(path)

    if not file_path.exists():
        raise ValueError("Filen finns inte")

    if not file_path.is_file():
        raise ValueError("Sökvägen är inte en fil")

    return file_path
