import psycopg2


def launch():
    connection = psycopg2.connect(dbname='testtask', user='postgres', password='admin', host='localhost', port='5432')
    cursor = connection.cursor()

    def profileInformationOutput(element):
        profileOutput = f"\"phone_number\":\"{element[0][0]}\",\"invite_code\":\"{element[0][1]}\",\"code\":\"{element[0][2]}\""
        profileOutput = "{" + profileOutput + "}"
        return profileOutput

    def absenceInformationOutput():
        return "{\"response\":\"no_user\"}"

    def elementQuery(phoneNumber):
        query = f"SELECT phone_number,invite_code,code FROM users WHERE phone_number = '{phoneNumber}'"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def elementExist(element):
        elementNumber = len(element)
        return elementNumber > 0

    def elementFunctionCall(elementExist):
        if elementExist:
            return profileInformationOutput(element)
        else:
            return absenceInformationOutput()

    element = elementQuery(phoneNumber)
    elementExist = elementExist(element)
    response = elementFunctionCall(elementExist)

    cursor.close()
    connection.close()

    return response