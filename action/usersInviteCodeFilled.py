import psycopg2

def launch():
    response = "{\"phone_numbers\":["
    connection = psycopg2.connect(dbname='testtask', user='postgres', password='admin', host='localhost', port='5432')
    cursor = connection.cursor()
    query = "SELECT phone_number FROM public.users WHERE invite_code IS NOT null"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        response += f"\"{row[0]}\","
    cursor.close()
    connection.close()
    response = response[:len(response)-1] + "]}"

    return response