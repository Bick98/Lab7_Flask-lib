from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.statistic_model import borrowers, most_pop_book, most_pop_zhanr



@app.route('/statistics', methods=['get'])
def statistics():
    conn = get_db_connection()

    selected = ['Должники', 'Самый популярный жанр']

    if request.values.get('select'):
        choice = request.values.get('select')
    else:
        choice = ''

    if choice == 'Должники':
        flag = 1
        df_bor = borrowers(conn)
        df_pop = []
    elif choice == 'Самый популярный жанр':
        zhanr = most_pop_zhanr(conn).values[0][0]
        df_pop = most_pop_book(conn,zhanr)
        flag = 2
        df_bor = []
    else:
        flag = 0
        df_bor = []
        df_pop = []








    html = render_template(
        'statistics.html',
        df_borrowers=df_bor,
        df_most_pop=df_pop,
        f=flag,
        selected=selected,
        len=len
    )
    return html









# def statistics():
#     conn = get_db_connection()
#     borrowers_list=pandas.DataFrame
#     books_list=pandas.DataFrame
#     most_popular_book_df=pandas.DataFrame
#     if request.values.get('submitGetBorrowers'):
#         startDate=request.values.get('dateStart')
#         endDate=request.values.get('dateEnd')
#         startDate=convert_date(startDate)
#         endDate=convert_date(endDate)
#         borrowers_list=borrowers(conn, startDate, endDate)
#         print(borrowers_list)
#         return render_template('statistics.html',
#                                borrowers_list=borrowers_list,
#                                most_popular_book_df=most_popular_book_df,
#                                len=len
#                                )
#     elif request.values.get('submitGetPopularBook'):
#         startDate=request.values.get('dateStart')
#         endDate=request.values.get('dateEnd')
#         startDate=convert_date(startDate)
#         endDate=convert_date(endDate)
#         books_list=most_popular_book(conn, startDate, endDate)
#         print(books_list)
#     return render_template('statistics.html',
#                            most_popular_book_df=books_list,
#                                borrowers_list=borrowers_list,
#                                len=len)