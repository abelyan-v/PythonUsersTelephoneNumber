import psycopg2

class inviteCodeInsert():

    connection = psycopg2.connect(dbname='testtask', user='postgres', password='admin', host='localhost', port='5432')
    cursor = connection.cursor()

    def removeInviteCode(self):
        query = f"DELETE FROM public.invite_code WHERE code = '{self.code}'"
        self.cursor.execute(query)
        self.connection.commit()
        self.response = "{\"response\":\"success\"}"

    def inviteCodeInsert(self):
        query = f"UPDATE public.\"users\" SET invite_code = '{self.code}' WHERE phone_number = '{self.phoneNumber}'"
        self.cursor.execute(query)
        self.connection.commit()
        self.removeInviteCode()

    def inviteCodeExistCall(self,inviteCodeExist):
        if inviteCodeExist:
            self.inviteCodeInsert()
        else:
            self.response = "{\"response\":\"invite_code_error\"}"

    def inviteCodeExist(self):
        query = f"SELECT * FROM public.invite_code WHERE code='{self.code}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return len(result) > 0

    def enteredInviteCodeCall(self):
        if self.enteredInviteCode:
            self.response = "{\"response\":\"invite_code_exist\"}"
        else:
            inviteCodeExist = self.inviteCodeExist()
            self.inviteCodeExistCall(inviteCodeExist)


    def enteredInviteCodeCheck(self):
        self.enteredInviteCode = self.result[0][1] != None


    def userExist(self):
        query = f"SELECT phone_number,invite_code FROM public.\"users\" WHERE phone_number = '{self.phoneNumber}'"
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        return len(self.result) > 0


    def userExistCall(self,userExist):
        if userExist:
            self.enteredInviteCodeCheck()
            self.enteredInviteCodeCall()
        else:
            self.response = "{\"response\":\"no_user\"}"


def launch():
    inviteCodeInset = inviteCodeInsert()
    inviteCodeInset.phoneNumber = phoneNumber
    inviteCodeInset.code = code
    userExist = inviteCodeInset.userExist()
    inviteCodeInset.userExistCall(userExist)
    response = inviteCodeInset.response

    inviteCodeInset.cursor.close()
    inviteCodeInset.connection.close()

    return response