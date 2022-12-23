

def addcart(skuId,number):
    if skuId != None and number != None:
        if skuId=='591' and number=='1':#添加购物车成功
            return {'code': '200','message': '成功'}
        else: #添加购物车失败
            return
    return {'code': '200','message': '成功'}
