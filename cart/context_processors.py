from .cart import Cart


#create context processor so our cart can work all pages 
def cart(request):
    #Return the defalut data from our cart
    return{'cart':Cart(request)}