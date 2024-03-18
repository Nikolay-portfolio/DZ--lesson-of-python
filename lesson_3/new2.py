from new import Address
class Mailing:
    to_address = 'Address'
    from_address = 'Address'
    cost = '000'
    track = " "
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
         
    def letter(self):
        print("Отправление", self.track, "из" , self.index , self.city , self.street , self.home , self.kv , 
        "в" ,self.index , self.city , self.street , self.home , self.kv ,"Стоимость " , self.cost , "рублей")

        
    
