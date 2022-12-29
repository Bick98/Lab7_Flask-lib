import pandas
import sqlite3

def borrowers(conn):
    return pandas.read_sql(f'''
        SELECT distinct reader_name AS 'Имя_должника'
        FROM reader
        JOIN book_reader USING (reader_id)
        WHERE return_date IS NULL 
    ''', conn)


def most_pop_zhanr(conn):
    return pandas.read_sql(f'''SELECT genre_id,
    SUM(available_numbers) AS sum_amount
    FROM book
    GROUP BY genre_id
    ORDER BY sum_amount DESC LIMIT 1
    ''',conn)


def most_pop_book(conn,zhanr):
    return pandas.read_sql(f'''
    WITH get_authors(book_id, authors_name)
    AS(
    SELECT book_id, GROUP_CONCAT(author_name)
    FROM AUTHOR JOIN book_author USING(author_id)
    GROUP BY book_id)
    SELECT 
    title AS Название,
    authors_name AS Авторы,
    genre_name AS Жанр
    FROM book
    LEFT JOIN get_authors USING (book_id)
    LEFT JOIN genre USING (genre_id)
    WHERE book.genre_id = :zh  
    ''',conn, params={"zh": int(zhanr)})


    # Статисткика: 1)
    # Поле со списком в нём, все должники без повторений
    #
    # 2) Книги с популярным жанром + авторы в 1 строчке