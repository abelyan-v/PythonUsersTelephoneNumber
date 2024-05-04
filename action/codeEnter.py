import psycopg2

def launch():
    connection = psycopg2.connect(dbname='testtask', user='postgres', password='admin', host='localhost', port='5432')
    cursor = connection.cursor()

    query = f"SELECT phone_number,invite_code,code FROM public.users WHERE phone_number = '{phoneNumber}'"
    cursor.execute(query)
    result = cursor.fetchall()
    if len(result) > 0:
        if userCode == result[0][2]:
            query = f"UPDATE public.users SET code = NULL WHERE phone_number = '{phoneNumber}'"
            cursor.execute(query)
            connection.commit()
            if len(result[0][2]) == 4:
                response = "{\"response\":\"authorisation_code_success\"}"
            else:
                response = "{\"response\":\"registration_code_success\"}"
        else:
            response = "{\"response\":\"code_error\"}"
    else:
        response = "{\"response\":\"user_not_found\"}"

    cursor.close()
    connection.close()

    return response