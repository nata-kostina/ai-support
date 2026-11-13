import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import psycopg
from psycopg.rows import dict_row

from app.config import settings


def connect() -> psycopg.Connection:
    return psycopg.connect(
        settings.database_url,
        autocommit=True,
        row_factory=dict_row,  # type: ignore
    )


def start_event(gmail_message_id: str) -> dict | None:
    """Claim a message. Returns None when it is already handled or in progress."""
    with connect() as conn:
        return conn.execute(
            """
            insert into events (gmail_message_id) values (%s)
            on conflict (gmail_message_id) do update
              set attempts = events.attempts + 1, status = 'processing', error = null
              where events.status = 'failed'
            returning id, attempts
            """,
            (gmail_message_id,),
        ).fetchone()  # type: ignore


if __name__ == "__main__":
    test_message_id = "test_gmail_msg_12345"

    print("--- 1. Первая попытка вставить событие ---")
    result_first = start_event(test_message_id)
    print(f"Результат первого вызова: {result_first}")
    # Ожидается: словарь с id и attempts (например, {'id': 1, 'attempts': 1}),
    # так как записи еще не было, она успешно создалась со статусом 'processing'.

    print("\n--- 2. Вторая попытка вставить событие с ТЕМ ЖЕ ID ---")
    result_second = start_event(test_message_id)
    print(f"Результат второго вызова: {result_second}")
    # Ожидается: None.
    # Почему? Потому что запись уже существует, и ее текущий статус — 'processing'
    # (а условие WHERE events.status = 'failed' в SQL-запросе не выполняется).
    # Следовательно, база ничего не возвращает (returning id, attempts дает пустоту).
