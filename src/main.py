import os
import sys
import mysql.connector
from json import dumps
from sendy.api import SendyAPI
from mysql.connector import Error
from src.log import Logger, data_log
from src.queries import Queries as query
from src.alert import google_chat_alert

LOG = Logger()

MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
SENDY_URL = os.getenv('SENDY_URL')
SENDY_API_KEY = os.getenv('SENDY_API_KEY')
SENDY_LIST_KEY = os.getenv('SENDY_LIST_KEY')

def handler(event, context):
    LOG.info(f'Event: {dumps(event)}')
    if event['command'] == 'addSubscribers':
        records = get_subs()
        subs_count, invalid_subs_count = add_subs(records)
        google_chat_alert(subs_count, invalid_subs_count)

def get_subs():
    try:
        LOG.info(f'Connecting to the database {MYSQL_DATABASE}')
        conn = mysql.connector.connect(host=MYSQL_HOST,
                                            port=MYSQL_PORT,
                                            database=MYSQL_DATABASE,
                                            user=MYSQL_USER,
                                            password=MYSQL_PASSWORD)
        LOG.info('Set cursor')
        cursor = conn.cursor()
        LOG.info('Execute query')
        cursor.execute(query.cp_subscribers_last7days)
        LOG.info('Fetch data')
        records = cursor.fetchall()
        LOG.info(f'Total number of rows: {cursor.rowcount}')
        if cursor.rowcount == 0:
            LOG.error('Service will exit because no record of new registrations was found')
            sys.exit()
        return records
    except Error as e:
        LOG.exception('Error reading data from MySQL table')

def close_conn(conn, cursor):
    if conn.is_connected():
        conn.close()
        cursor.close()
        LOG.info('MySQL connection is closed')

def add_subs(records):
    LOG.info(f'Adding new {MYSQL_DATABASE} subscribers')
    subs_list = []
    alreary_subs_list = []
    invalid_subs_list = []
    subs_count = 0
    already_subs_count = 0
    invalid_subs_count = 0
    for row in records:
        name = row[0]
        email = row[1]
        resp = sendy_subs(name, email)
        if resp == '1':
            subs_list.append(email)
            subs_count += 1
        elif resp == 'Already subscribed.':
            alreary_subs_list.append(email)
            already_subs_count += 1
        elif resp == 'Invalid email address.':
            invalid_subs_list.append(email)
            invalid_subs_count += 1
        elif resp == 'Invalid list ID.':
            LOG.error(resp)
            sys.exit()
    data_log = data_log(subs_list, subs_count, alreary_subs_list, already_subs_count, invalid_subs_list, invalid_subs_count)
    LOG.info(f'''Emails were successfully inserted: {data_log}''')
    return subs_count, invalid_subs_count

def sendy_subs(name, email):
    try:
        api = SendyAPI(
            host=SENDY_URL,
            api_key=SENDY_API_KEY,
        )
        response = api.subscribe(
            list=SENDY_LIST_KEY,
            email=email,
            name=name
        )
        return response
    except Exception as e:
        LOG.exception('Error inserting emails in the list')

# To test locally
if __name__ == '__main__':
    event = {"command": "addSubscribers"}
    handler(event, context = None)
