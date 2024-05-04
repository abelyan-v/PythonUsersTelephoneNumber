import psycopg2
import random

def launch():
    code = ""

    connection = psycopg2.connect(dbname='testtask', user='postgres', password='admin', host='localhost', port='5432')
    cursor = connection.cursor()

    query = f"SELECT phone_number,invite_code,code FROM public.users WHERE phone_number='{phoneNumber}'"
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) > 0:
        if len(result[0][2]) == 6:
            for i in range(6):
                code += str(random.randrange(10))
            query = f"UPDATE public.users SET code='{code}' WHERE phone_number='{phoneNumber}'"
            cursor.execute(query)
            connection.commit()
            response = "{\"response\":\"registration_is_not_completed\"}"
        else:
            for i in range(4):
                code += str(random.randrange(10))
            query = f"UPDATE public.users SET code='{code}' WHERE phone_number='{phoneNumber}'"
            cursor.execute(query)
            connection.commit()
            response = "{\"response\":\"sign_in_user\"}"
    else:
        for i in range(6):
            code += str(random.randrange(10))
        query = f"INSERT INTO public.users (phone_number,code) VALUES ('{phoneNumber}','{code}')"
        cursor.execute(query)
        connection.commit()
        response = "{\"response\":\"sign_up_user\"}"

    cursor.close()
    connection.close()

    return response