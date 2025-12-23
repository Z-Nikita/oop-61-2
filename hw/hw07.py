import sqlite3

DB_NAME = "movies.db"
TABLE_NAME = "movies"

def get_connection():
    """Создаёт подключение к базе."""
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn

def init_db():
    """Создаёт таблицу, если её ещё нет."""
    with get_connection() as conn:
        conn.execute(f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                title  TEXT NOT NULL,
                genre  TEXT NOT NULL,
                year   INTEGER NOT NULL,
                rating REAL NOT NULL CHECK(rating >= 0 AND rating <= 10)
            )
        """)
        conn.commit()

# CRUD

def create_movie(title, genre, year, rating):
    """Create: добавление записи. Возвращает rowid новой записи."""
    if not str(title).strip() or not str(genre).strip():
        raise ValueError("title и genre не должны быть пустыми.")
    if year < 1900 or year > 2025:
        raise ValueError("year должен быть в диапазоне 1900..2025.")
    if not (0 <= rating <= 10):
        raise ValueError("rating должен быть от 0 до 10.")

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO {TABLE_NAME} (title, genre, year, rating) VALUES (?, ?, ?, ?)",
            (str(title).strip(), str(genre).strip(), year, rating),
        )
        conn.commit()

        return cur.lastrowid  # это rowid


def read_all_movies():
    """Read: получить все записи (с rowid)."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT rowid, title, genre, year, rating FROM {TABLE_NAME} ORDER BY rowid")

        return cur.fetchall()

def get_by_rowid(row_id):
    """Доп. задание: получить одну запись по rowid."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            f"SELECT rowid, title, genre, year, rating FROM {TABLE_NAME} WHERE rowid = ?",
            (row_id,),
        )
        return cur.fetchone()

def update_movie(row_id, title, genre, year, rating):
    """Update: обновить запись по rowid. Возвращает True, если запись обновилась."""
    if not str(title).strip() or not str(genre).strip():
        raise ValueError("title и genre не должны быть пустыми.")
    if year < 1900 or year > 2025:
        raise ValueError("year должен быть в диапазоне 1900..2025.")
    if not (0 <= rating <= 10):
        raise ValueError("rating должен быть от 0 до 10.")

    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            f"""
            UPDATE {TABLE_NAME}
               SET title = ?, genre = ?, year = ?, rating = ?
             WHERE rowid = ?
            """,
            (str(title).strip(), str(genre).strip(), year, rating, row_id),
        )
        conn.commit()

        return cur.rowcount > 0

def delete_movie(row_id):
    """Delete: удалить запись по rowid. Возвращает True, если запись удалена."""
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {TABLE_NAME} WHERE rowid = ?", (row_id,))
        conn.commit()

        return cur.rowcount > 0

# Небольшое меню для проверки

def _print_movies(rows):
    if not rows:
        print("Таблица пустая.")
        return

    print("\nrowid | title | genre | year | rating")
    print("-" * 50)
    for r in rows:
        rowid, title, genre, year, rating = r
        print(f"{rowid:5d} | {title} | {genre} | {year} | {rating}")

def _read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Введите целое число.")

def _read_float(prompt):
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("Введите число.")

def main():
    init_db()

    while True:
        print("\n=== Movies DB (SQLite CRUD) ===")
        print("1) Create (add movie)")
        print("2) Read (show all)")
        print("3) Get by rowid (one movie)")
        print("4) Update by rowid")
        print("5) Delete by rowid")
        print("0) Exit")

        choice = input("Выберите пункт: ").strip()

        try:
            if choice == "1":
                title = input("Название: ")
                genre = input("Жанр: ")
                year = _read_int("Год (1900..2025): ")
                rating = _read_float("Рейтинг (0..10): ")
                new_id = create_movie(title, genre, year, rating)
                print(f"Добавлено! rowid = {new_id}")

            elif choice == "2":
                rows = read_all_movies()
                _print_movies(rows)

            elif choice == "3":
                rid = _read_int("Введите rowid: ")
                row = get_by_rowid(rid)
                if row:
                    _print_movies([row])
                else:
                    print("Запись не найдена.")

            elif choice == "4":
                rid = _read_int("Введите rowid для обновления: ")
                existing = get_by_rowid(rid)
                if not existing:
                    print("Запись не найдена.")
                    continue

                print("Введите новые значения:")
                title = input("Название: ")
                genre = input("Жанр: ")
                year = _read_int("Год (1900..2025): ")
                rating = _read_float("Рейтинг (0..10): ")

                ok = update_movie(rid, title, genre, year, rating)
                print("Обновлено!" if ok else "Не удалось обновить.")

            elif choice == "5":
                rid = _read_int("Введите rowid для удаления: ")
                ok = delete_movie(rid)
                print("Удалено!" if ok else "Запись не найдена.")

            elif choice == "0":
                print("До скорой встречи!")
                break

            else:
                print("Неизвестная команда.")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()