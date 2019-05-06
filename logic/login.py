from dbMoudle.student import Student


def onLogin(data):
    """
    data: dict
    """
    ret = {'ispass': False, 'account': "", 'name': "", 'avater': ""}
    account = data.setdefault('account', '')
    pwd = data.setdefault('pwd', '')
    user = Student.query.filter_by(account=account).first()
    if user is None or pwd != user.pwd:
        return ret
    ret['ispass'] = True
    ret['account'] = user.account
    ret['name'] = user.name
    ret['avater'] = user.avater
    return ret
