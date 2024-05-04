from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def userAuthorisation(request, phoneNumber):
    from action import userAuthorisation
    userAuthorisation.phoneNumber = f"+{phoneNumber}"
    response = userAuthorisation.launch()
    return HttpResponse(response)


def codeEnter(request, phoneNumber, code):
    from action import codeEnter
    codeEnter.phoneNumber = f"+{phoneNumber}"
    codeEnter.userCode = code
    response = codeEnter.launch()
    return HttpResponse(codeEnter.response)


def usersRequest(request, phoneNumber):
    from action import usersRequest
    usersRequest.phoneNumber = f"+{phoneNumber}"
    response = usersRequest.launch()
    return HttpResponse(response)


def inviteCodeInsert(request, phoneNumber, inviteCode):
    from action import insertInviteCode
    insertInviteCode.phoneNumber = f"+{phoneNumber}"
    insertInviteCode.code = inviteCode
    response = insertInviteCode.launch()
    return HttpResponse(response)


def usersInviteCodeFilled(request):
    from action import usersInviteCodeFilled
    response = usersInviteCodeFilled.launch()
    return HttpResponse(response)