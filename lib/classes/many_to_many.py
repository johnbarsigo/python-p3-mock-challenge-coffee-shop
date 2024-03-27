class Coffee:

    total = []

    def __init__(self, name):
        self.name = name
        self.customer_list = []
        Coffee.total.append( self )

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):

        if not isinstance(value, str):

            raise ValueError("Name must be a string")
        
        if len(value) < 3:

            raise ValueError("Name length must be be greater or equal to 3 characters")
        
        if hasattr(self, '_name') and self._name is not None:
            raise AttributeError("Cannot change the name of the coffee")
        
        
        self._name = value
        
    def orders(self):

        return [ order for order in Order.total if order.coffee == self ]
        # pass
    
    def customers(self):

        return list ( set( [ order.customer for order in self.orders() ] ) )
        # pass
    
    def num_orders( self, customer ):

        if customer not in self.customer_list:
            self.customer_list.append ( customer )
        # pass
    
    def average_price ( self ) :

        total_price = sum ( order.price for order in self.orders() )

        return total_price / len ( self.orders() ) if self.orders() else None
        # pass

class Customer:

    total = []

    def __init__(self, name):

        self.name = name
        self.orders_list = []
        Customer.total.append ( self )

    
    @property
    def name ( self ) :

        return self._name
    
    @name.setter
    def name ( self, value ) :

        if not isinstance ( value, str ) :

            raise ValueError("Name must be a string")
        
        if len ( value ) > 15:

            raise ValueError ( "Name must be 15 characters or less" )
        
        self._name = value
        
    def orders(self):

        return [ order for order in Order.total if order.customer == self ]
        # pass
    
    def coffees(self):

        return list( set( [ order.coffee for order in self.orders() ] ) )
        # pass
    
    def create_order(self, coffee, price) :

        created_order = Order ( self, coffee, price )
        return created_order
        # pass

    
class Order:

    total = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

        Order.total.append(self)
    
    def get_price ( self ) :

        return self._price

    def set_price ( self, val ) :

        if isinstance ( val, float ) and 1.0  <= val <= 10.0 and not hasattr ( self, 'price' ) :

            self._price = val

    price = property(get_price, set_price)