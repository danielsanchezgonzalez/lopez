import os
import psycopg2
import requests
import random

from pdf2image import convert_from_path


def connect_db(url: str="postgres://lopez:lopez&asociados@170.187.136.45:5432/cct") -> None:
    """
    Este metodo conecta a la base de datos
    """
    
    conn = psycopg2.connect(url)
    cur = conn.cursor()
    return conn, cur


def close_db(conn, cur) -> None:
    """
    Este metodo cierra la conexion con la base de datos
    """
    conn.commit()

    cur.close()
    conn.close()

conn, cur = connect_db()

urls_query = f'SELECT url FROM cct_web;'
cur.execute(urls_query)
urls = [url[0] for url in cur.fetchall()]

for url in urls:

    response = requests.get(url, verify=False)

    with open('tmp.pdf', 'wb') as file:
        file.write(response.content)

    print(f'file {urls.index(url)}')

close_db(conn, cur)