import logging
from scraper import (
    fetch_multiple_book_pages,
    fetch_book_detail,
    remove_duplicate_books,
)
from save_csv import save_books_to_csv
from save_json import save_books_to_json
from save_failed_csv import save_failed_books_to_csv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def main() -> None:
    start_url = "https://books.toscrape.com/"
    books = fetch_multiple_book_pages(start_url, max_pages=3)

    if not books:
        logging.warning("商品を取得できませんでした")
        return

    logging.info(f"重複除去前: {len(books)} 件")
    books = remove_duplicate_books(books)

    # テスト用に失敗URLを1件追加したいとき
    books.append({
        "title": "test book",
        "detail_url": "https://books.toscrape.com/catalogue/not-found_9999/index.html",
        "price": "",
        "stock": "",
        "rating": "",
    })

    success_books = []
    failed_books = []

    for book in books:
        detail = fetch_book_detail(book["detail_url"])
        book.update(detail)

        if book.get("upc") or book.get("description") or book.get("category"):
            success_books.append(book)
            logging.info(f"詳細取得成功: {book['title']}")
        else:
            failed_books.append(book)
            logging.warning(f"詳細取得失敗: {book['detail_url']}")

    logging.info(f"成功件数: {len(success_books)}")
    logging.info(f"失敗件数: {len(failed_books)}")

    save_books_to_csv(success_books, "data/books_success.csv")
    save_books_to_json(success_books, "data/books_success.json")
    logging.info("成功データ保存完了")

    save_failed_books_to_csv(failed_books, "data/books_failed.csv")
    logging.info("失敗データ保存完了")


if __name__ == "__main__":
    main()