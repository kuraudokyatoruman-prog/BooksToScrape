import csv
from pathlib import Path


def save_failed_books_to_csv(failed_books: list[dict[str, str]], file_path: str) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "detail_url", "fetched_at", "source_url"])

        for book in failed_books:
            writer.writerow([
                book.get("title", ""),
                book.get("detail_url", ""),
                book.get("fetched_at", ""),
                book.get("source_url", "")
            ])