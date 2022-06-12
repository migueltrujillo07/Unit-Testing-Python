class ProductDiscountError(Exception):
    pass


class Product:

    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        self.discount = discount
        
        if discount > price:
            raise ProductDiscountError('Sorry but the discount can not be more than the price')
        
        
    @property
    def code(self):
        return f'code-{self.name}'

