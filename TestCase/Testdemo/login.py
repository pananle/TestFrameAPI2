

#登录功能
def login(phone,verificationCode):
    if phone!=None and verificationCode!=None:
        if phone=='15738051864' and verificationCode=='9999':#账号密码正确登录成功
            return {'code': '200','message': '成功'}
        else:#账号密码错误
            return {'code': '11005','message': '验证码有误'}
    return {'code': '11005','message': '验证码有误'}#账号或密码为空

